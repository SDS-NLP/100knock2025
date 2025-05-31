import pandas as pd
import os
import requests
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
import pandas as pd

# カラム名を指定して読み込む
columns = ['question', 'A', 'B', 'C', 'D', 'answer']
df = pd.read_csv("/home/tanxin/100knock2025/xin/chapter05/anatomy.csv", header=None, names=columns)

# カラム名付きで上書き保存
df.to_csv("anatomy.csv", index=False)


correct = 0
total = 0

for idx, row in df.iterrows():
    # 問題文と選択肢を整形
    prompt = f"次の解剖学の問題に答えてください。\n{row['question']}\n"
    for label in ['A', 'B', 'C', 'D']:
        prompt += f"{label}. {row[label]}\n"
    prompt += "正解をA〜Dの中から1つ選んでください。"

    # API呼び出し
    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.0
        }
    )

    result = response.json()
    print(result)
    if "choices" not in result:
        print("APIエラー:", result)
        continue 
    answer_text = result["choices"][0]["message"]["content"].strip()

    # モデルの回答（A〜D）を抽出
    selected = next((label for label in ['A', 'B', 'C', 'D'] if label in answer_text), None)

    if selected == row['answer']:
        correct += 1
    total += 1

accuracy = correct / total * 100
print(f"\n 正解率: {accuracy:.2f}%（{correct}問 / {total}問）")


