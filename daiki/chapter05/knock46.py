import requests
import json

# APIキーを読み込み
with open("/Users/aa/100knock2025/daiki/chapter05/gemini_apikey.txt", "r") as f:
    API_KEY = f.read().strip()

# APIエンドポイント
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# テーマ設定（自由に変更可）
theme = "夏"

# リクエスト内容
headers = {
    "Content-Type": "application/json"
}

data = {
    "contents": [
        {
            "parts": [
                {
                    "text": f"テーマ「{theme}」で川柳を10個作ってください。"
                }
            ]
        }
    ]
}

# APIリクエスト送信
response = requests.post(url, headers=headers, data=json.dumps(data))

# 応答の処理
if response.status_code == 200:
    result = response.json()
    content = result["candidates"][0]["content"]["parts"][0]["text"]
    print("生成された川柳:\n")
    print(content)
else:
    print(f"エラー: {response.status_code}")
    print(response.text)
