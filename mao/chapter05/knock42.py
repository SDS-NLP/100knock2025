"""
knock42：多岐選択問題の正解率
JMMLU のいずれかの科目を大規模言語モデルに解答させ、その正解率を求めよ。
"""
import pandas as pd
import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

# APIキー読み込み
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Geminiモデル設定
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# CSVファイルを読み込む（ヘッダーなしなので列名を明示）
df = pd.read_csv("mao/chapter05/astronomy.csv", header=None,
                 names=["Question", "A", "B", "C", "D", "Answer"])

labels = ["A", "B", "C", "D"]
correct_count = 0

# 各行に対して推論
for i, row in df.iterrows():
    question = row["Question"]
    choices = [row["A"], row["B"], row["C"], row["D"]]
    correct = row["Answer"].strip()

    # 選択肢テキストを作成
    choices_text = "\n".join([f"{label}. {choice}" for label, choice in zip(labels, choices)])

    # プロンプト
    prompt = f"""
問題: {question}
選択肢:
{choices_text}

正解をA-Dのアルファベットで答えてください。
ただし、アルファベット1文字のみで答え、他の言葉は一切付け加えないでください。
"""

    # モデルに送信
    try:
        response = model.generate_content(prompt)
        answer = response.text.strip().upper()[0]  # 最初の1文字だけ取得
    except Exception as e:
        print(f"Q{i+1}: エラー - {e}")
        continue

    print(f"Q{i+1}: モデルの回答: {answer} / 正解: {correct}")

    if answer == correct:
        correct_count += 1

    time.sleep(5)  # クォータ対策

# 最終結果
accuracy = correct_count / len(df)
print(f"\n--- 結果 ---")
print(f"正解数: {correct_count} / {len(df)}")
print(f"正解率: {accuracy:.2%}")
