import requests
import os
from dotenv import load_dotenv

# .envファイル読み込み
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("❌ '.env' に GROQ_API_KEY が設定されていません。")

# API情報
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# prompt.txt を1行ずつ読み込んで処理
try:
    with open("prompt.txt", "r", encoding="utf-8") as file:
        prompts = [line.strip() for line in file if line.strip()]
except FileNotFoundError:
    raise FileNotFoundError("❌ 'prompt.txt' が見つかりません。")

# 各プロンプトに対してAPIリクエストを送る
for i, prompt in enumerate(prompts, 1):
    print(f"\n🧠 プロンプト {i}: {prompt}")

    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        try:
            answer = response.json()["choices"][0]["message"]["content"]
            print(f"✅ 回答 {i}:\n{answer}")
        except Exception as e:
            print(f"❌ 回答解析エラー（{i}行目）:", e)
    else:
        print(f"❌ APIエラー（{i}行目）:", response.status_code, response.text)
