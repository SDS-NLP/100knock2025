import openai
import csv

with open("key.txt", "r") as f:
    api_key = f.read().strip()

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

def load_anatomy_data(filepath="anatomy.csv"):
    """
    anatomy.csv を読み込んで、(question, choices, correct_label) のリストを返す。
    - question: str（設問文）
    - choices: list[str]（選択肢4つ）
    - correct_label: str（"A"〜"D"）
    """
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames

        question_key = fieldnames[0]
        choices_keys = fieldnames[1:-1]
        answer_key = fieldnames[-1]

        data = []

        for row in reader:
            question = row[question_key].strip()
            choices = [row[k].strip() for k in choices_keys]
            correct_label = row[answer_key].strip().upper()
            data.append((question, choices, correct_label))

        return data

# 🔹 メイン実行部（評価用）
if __name__ == "__main__":
    data = load_anatomy_data()

    correct = 0
    total = 0

    for question, choices, correct_answer in data:
        total += 1
        choice_labels = ["A", "B", "C", "D"]
        choice_lines = [f"{label}. {text}" for label, text in zip(choice_labels, choices)]

        # プロンプト
        prompt = f"次の問いに答えてください。\n\nQ: {question}\n" + "\n".join(choice_lines) + "\n\n答えは？"

        print(f"{total}問目を処理中...", end="\r")

        # LLMに質問
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        reply = response.choices[0].message.content.strip().upper()

        # 回答が正解を含んでいたらカウント
        if correct_answer in reply:
            correct += 1

    # 結果表示
    print()  # 改行
    print(f"正解数: {correct} / {total}")
    print(f"正解率: {correct / total:.2%}")
