import pandas as pd
import requests
import json

# 元のデータ読み込み
df = pd.read_csv("high_school_physics.csv")

# 列名の特定（日本語列なのでインデックスで取得）
columns = df.columns.tolist()
question_col = columns[0]
choice_cols = columns[1:5]  # A, B, C, D
answer_col = columns[5]

# コピーを作る
df_modified = df.copy()

# 正解をDに固定
for i, row in df.iterrows():
    correct_label = row[answer_col].strip().upper()
    if correct_label not in ["A", "B", "C", "D"]:
        continue  # スキップ

    # 正解とDの内容を入れ替え
    correct_index = ord(correct_label) - ord("A")  # A=0, B=1, ...
    d_index = 3  # Dのインデックス

    # 入れ替え
    df_modified.iat[i, 1 + correct_index], df_modified.iat[i, 1 + d_index] = row[choice_cols[d_index]], row[choice_cols[correct_index]]

    # 正解列を "D" に変更
    df_modified.iat[i, 5] = "D"

# 保存（任意）
df_modified.to_csv("high_school_physics_correct_D.csv", index=False)


# CSV読み込み
df = pd.read_csv("high_school_physics_correct_D.csv")

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