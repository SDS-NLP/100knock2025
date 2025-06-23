import requests
from dotenv import load_dotenv
import os
load_dotenv()  # .envファイルを読み込む
API_KEY = os.getenv("GROQ_API_KEY")
# Groq API情報
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# 問題文の設定
prompt = """
適当なお題を設定し、川柳の案を10個作成せよ。
"""

# API呼び出し
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.8
}

response = requests.post(API_URL, headers=headers, json=payload)

# 結果の取得と表示
result = response.json()
output = result["choices"][0]["message"]["content"]
print("モデルの回答:", output)