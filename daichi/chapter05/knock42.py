import os
from dotenv import load_dotenv
import google.generativeai as genai
import pandas as pd
import time

# .env から API キーを取得
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# モデル設定
model = genai.GenerativeModel("models/gemini-1.5-flash")

# データ読み込み
df = pd.read_csv("/Users/daichisakamoto/code/100knock2025/daichi/chapter05/japanese_history.csv")
df.columns = df.columns.str.strip()

# 正解カウント
correct = 0

for idx, row in df.iterrows():
    question = row[df.columns[0]]
    options = [row[df.columns[1]], row[df.columns[2]], row[df.columns[3]], row[df.columns[4]]]
    correct_answer = row[df.columns[5]].strip()

    prompt = f"""
以下は日本史の多肢選択問題です。最も適切な選択肢を A〜D の中から1つ選んでください。

Q. {question}

A. {options[0]}
B. {options[1]}
C. {options[2]}
D. {options[3]}

正解の選択肢を A, B, C, D から1つだけ記してください。
"""
    try:
        response = model.generate_content(prompt)
        text = response.text.strip()
        if correct_answer in text:
            correct += 1
    except Exception as e:
        print(f"❌ Error at index {idx}: {e}")
        continue
    time.sleep(1.2)  # クォータ回避

# 正解率の計算と出力
accuracy = correct / len(df)
print(f"正解率: {accuracy:.2%}")
