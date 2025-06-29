import pandas as pd
import os
import requests
import time
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

columns = ['question', 'A', 'B', 'C', 'D', 'answer']
df = pd.read_csv("/home/tanxin/100knock2025/xin/chapter05/anatomy.csv", header=None, names=columns)

# カラム名付きで上書き保存
df.to_csv("anatomy.csv", index=False)


# すべての正解ラベルを 'D' に書き換え（正解がどの選択肢にあるかは変えない想定）
df['answer'] = 'D'

correct = 0
total = 0

for idx, row in df.iterrows():
    prompt = f"次の問題に答えてください。\n{row['question']}\n"
    for label in ['A', 'B', 'C', 'D']:
        prompt += f"{label}. {row[label]}\n"
    prompt += "正解をA〜Dの中から1つ選んでください。"

    response = requests.post(
        "https://api.groq.com/openai/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7,
        }
    )

    result = response.json()
    answer_text = result["choices"][0]["message"]["content"].strip()

    selected = next((label for label in ['A', 'B', 'C', 'D'] if label in answer_text), None)

    # 正解ラベルはすべてDなので、モデルがDを選べば正解
    if selected == 'D':
        correct += 1
    total += 1


accuracy = correct / total * 100
print(f"\n バイアス実験（正解全D）正解率: {accuracy:.2f}%（{correct}問 / {total}問）")
