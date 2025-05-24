import requests
import os
from dotenv import load_dotenv

# .envからAPIキーを取得
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("❌ .env に GROQ_API_KEY が設定されていません。")

# Groq API設定
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 問いかけ内容（プロンプト）
user_prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、
間違えて急行に乗車してしまったことに気付きました。
自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。

目的地の駅の名前を答えてください。
"""

# APIリクエスト
payload = {
    "model": MODEL,
    "temperature": 0,
    "messages": [
        {"role": "user", "content": user_prompt}
    ]
}

response = requests.post(API_URL, headers=headers, json=payload)

# 結果表示
if response.status_code == 200:
    answer = response.json()["choices"][0]["message"]["content"].strip()
    print("🧠 モデルの応答:")
    print(answer)
else:
    print("❌ APIリクエスト失敗:")
    print(response.status_code, response.text)