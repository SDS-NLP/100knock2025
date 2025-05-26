from knock42 import load_anatomy_data
import openai
import random

with open("key.txt", "r") as f:
    api_key = f.read().strip()

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

data = load_anatomy_data()

correct = 0
total = 0

for question, all_choices, correct_letter in data:
    total += 1
    correct_index = ["A", "B", "C", "D"].index(correct_letter)
    correct_text = all_choices[correct_index]

    # 正解以外をシャッフル
    other_choices = all_choices[:correct_index] + all_choices[correct_index+1:]
    random.shuffle(other_choices)
    randomized_choices = dict(zip(["A", "B", "C"], other_choices))
    randomized_choices["D"] = correct_text

    # 選択肢を組み立て
    choice_lines = [f"{k}. {v}" for k, v in randomized_choices.items()]

    # プロンプト
    prompt = f"次の問いに答えてください。\n\nQ: {question}\n" + "\n".join(choice_lines) + "\n\n答えは？"

    print(f"{total}問目を処理中...", end="\r")

    # LLM実行
    response = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    reply = response.choices[0].message.content.strip().upper()

    if "D" in reply:
        correct += 1

# 結果表示
print()
print(f"[正解をDに固定] 正解数: {correct} / {total}")
print(f"[正解をDに固定] 正解率: {correct / total:.2%}")
