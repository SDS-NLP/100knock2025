import pandas as pd
import google.generativeai as genai
import time
from dotenv import load_dotenv
import os

# .env ファイルから API_KEY を読み込み
load_dotenv()
api_key = os.getenv("API_KEY")

# Gemini API の初期化
genai.configure(api_key=api_key)
model = genai.GenerativeModel('models/gemini-2.0-flash')

# CSVファイル読み込み
df = pd.read_csv('astronomy.csv')

# 解答と正解判定
correct = 0
model_answers = []

for idx, row in df.iterrows():
    prompt = f"""以下の質問に最も適した選択肢を1つ選んでください（A〜Dの形式で答えてください）：
質問: {row['question']}
A: {row['A']}
B: {row['B']}
C: {row['C']}
D: {row['D']}
答えは1文字で（A/B/C/D）答えてください。"""

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip().upper()
        selected = answer[0]  # 最初の1文字を取り出し

        model_answers.append(selected)

        if selected == row['answer'].strip().upper():
            correct += 1

    except Exception as e:
        print(f"Error at index {idx}: {e}")
        model_answers.append("")

    time.sleep(1)  # 必要に応じて

# 結果表示
total = len(df)
accuracy = correct / total * 100
print(f"正解数: {correct} / {total}")
print(f"正解率: {accuracy:.2f}%")

