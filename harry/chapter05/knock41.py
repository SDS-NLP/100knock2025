import requests
import os
from dotenv import load_dotenv

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("❌ APIキーが設定されていません。'.env' に GROQ_API_KEY を定義してください。")

# プロンプトを外部ファイルから読み込み
try:
    with open("prompt_fewshots.txt", "r", encoding="utf-8") as f:
        prompt = f.read()
except FileNotFoundError:
    raise FileNotFoundError("❌ 'prompt.txt' が見つかりません。ファイルを作成してください。")

# Groq APIの情報
API_URL = "https://api.groq.com/openai/v1/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [
        {"role": "user", "content": prompt}
    ]
}

# リクエスト送信
response = requests.post(API_URL, headers=headers, json=payload)

# 結果表示
if response.status_code == 200:
    try:
        answer = response.json()["choices"][0]["message"]["content"]
        print("✅ 回答:")
        print(answer)
    except Exception as e:
        print("❌ レスポンス解析エラー:", e)
else:
    print("❌ APIリクエスト失敗:")
    print(response.status_code, response.text)
