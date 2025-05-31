import pandas as pd
import requests
import json

# CSV読み込み
df = pd.read_csv("high_school_physics.csv")

# 列名の自動抽出
columns = df.columns.tolist()
question_col = columns[0]
choice_cols = columns[1:5]   # A, B, C, D に相当する列
answer_col = columns[5]      # 正解ラベル（A〜D）

# APIキーの読み込み
with open("/Users/aa/100knock2025/daiki/chapter05/gemini_apikey.txt", "r") as f:
    API_KEY = f.read().strip()

url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}


# モデルに問題を送って答えをもらう関数
def ask_gemini_mcq(question, choices):
    prompt = f"次の問題に答えてください。\n{question}\n"
    for label, choice in zip(["A", "B", "C", "D"], choices):
        prompt += f"{label}. {choice}\n"
    prompt += "正しい選択肢を A, B, C, D のいずれか1文字で答えてください。モデルの回答が不明でもA,B,C,Dのどれかを答えてください。"

    data = {
        "contents": [
            {
                "parts": [
                    {"text": prompt}
                ]
            }
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        res = response.json()
        text = res["candidates"][0]["content"]["parts"][0]["text"].strip()
        if text and text[0] in "ABCD":
            return text[0]
        else:
            print("⚠️ モデルの回答が不明：", text)
            return None
    except Exception as e:
        print("APIエラー:", e)
        return None


# 正解率の計算
correct = 0
total = 15

for i in range(total):
    row = df.iloc[i]
    question = row[question_col]
    choices = [row[col] for col in choice_cols]
    correct_answer = row[answer_col].strip().upper()

    model_answer = ask_gemini_mcq(question, choices)
    is_correct = model_answer == correct_answer

    print(f"Q{i+1}: {model_answer} == {correct_answer} → {'⭕️' if is_correct else '❌'}")

    if is_correct:
        correct += 1

print(f"\n正解率: {correct / total * 100:.2f}%")