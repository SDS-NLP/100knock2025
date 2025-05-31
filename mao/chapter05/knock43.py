"""
knock43:応答バイアス
問題42において、実験設定を変化させると正解率が変化するかどうかを調べよ。
実験設定の例としては、大規模言語モデルの温度パラメータ、プロンプト、多肢選択肢の順番、
多肢選択肢の記号などが考えられる。

正解の選択肢を全てDに入れ替えて解答させる例。
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

# CSV読み込み
df = pd.read_csv("mao/chapter05/astronomy.csv", header=None,
                 names=["Question", "A", "B", "C", "D", "Answer"])

labels = ["A", "B", "C", "D"]
correct_count = 0

# 応答バイアス実験：正解の選択肢を D に強制移動
for i, row in df.iterrows():
    question = row["Question"]
    original_choices = {
        "A": row["A"],
        "B": row["B"],
        "C": row["C"],
        "D": row["D"],
    }
    original_answer = row["Answer"].strip()

    # 正解の選択肢内容をDに入れ替え
    correct_choice_text = original_choices[original_answer]
    manipulated_choices = {
        "A": "（ダミー）",
        "B": "（ダミー）",
        "C": "（ダミー）",
        "D": correct_choice_text
    }

    choices_text = "\n".join([f"{label}. {manipulated_choices[label]}" for label in labels])

    prompt = f"""
問題: {question}
選択肢:
{choices_text}

正解をA-Dのアルファベットで答えてください。
ただし、アルファベット1文字のみで答え、他の言葉は一切付け加えないでください。
"""

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip().upper()[0]
    except Exception as e:
        print(f"Q{i+1}: エラー - {e}")
        continue

    print(f"Q{i+1}: モデルの回答: {answer} / 正解: D")

    if answer == "D":
        correct_count += 1

    time.sleep(30)  # クォータ制限回避

# 正解率出力
accuracy = correct_count / len(df)
print("\n--- 応答バイアス実験：すべてDが正解 ---")
print(f"正解数: {correct_count} / {len(df)}")
print(f"正解率: {accuracy:.2%}")
