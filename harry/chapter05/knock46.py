import requests
import os
from dotenv import load_dotenv

# APIキー読み込み
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# お題の入力（必要に応じて固定でもOK）
theme = input("🎯 川柳のお題を入力してください: ").strip()

# プロンプトの準備
prompt = f"""
以下のお題「{theme}」に関する川柳を10個作成してください。
・川柳は5-7-5の形式で、日本語でユーモアや風刺を交えてください。
・番号付きで出力してください（例: 1. 〇〇〇）
"""

payload = {
    "model": MODEL,
    "temperature": 0.7,
    "messages": [
        {"role": "system", "content": "あなたは日本語の川柳を創作する達人です。リズムとユーモアを大切にしてください。"},
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    content = response.json()["choices"][0]["message"]["content"].strip()
    print("\n🎴 川柳の案（10個）:")
    print(content)

    # ログファイル保存
    with open("senryu_log.txt", "w", encoding="utf-8") as f:
        f.write(f"お題: {theme}\n\n")
        f.write(content)
        print("\n✅ senryu_log.txt に保存しました。")
else:
    print("❌ APIエラー:", response.status_code, response.text)
