import requests
import os
from dotenv import load_dotenv

# .env から API キーを読み込み
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# neko.txt からテキストを読み込む
file_path = "neko.txt"
if not os.path.isfile(file_path):
    print("❌ neko.txt が見つかりません。スクリプトと同じフォルダにあるか確認してください。")
    exit()

with open(file_path, "r", encoding="utf-8") as f:
    text = f.read().strip()

# API への問い合わせ
payload = {
    "model": MODEL,
    "temperature": 0,
    "messages": [
        {"role": "user", "content": text}
    ]
}

response = requests.post(API_URL, headers=HEADERS, json=payload)

# トークン数を表示
if response.status_code == 200:
    response_data = response.json()

    # 出力内容（モデルの応答）
    output = response_data["choices"][0]["message"]["content"].strip()
    print("\n🧠 モデルの出力:")
    print(output)

    # トークン数の表示
    usage = response_data["usage"]
    print("\n📊 トークン数情報:")
    print(f"・入力トークン数（prompt_tokens）: {usage.get('prompt_tokens', 'N/A')}")
    print(f"・出力トークン数（completion_tokens）: {usage.get('completion_tokens', 'N/A')}")
    print(f"・合計トークン数（total_tokens）: {usage.get('total_tokens', 'N/A')}")
else:
    print("❌ APIエラー:")
    print(response.status_code)
    print(response.text)