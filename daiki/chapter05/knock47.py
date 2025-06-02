import requests
import json

# APIキーを読み込み
with open("/Users/aa/100knock2025/daiki/chapter05/gemini_apikey.txt", "r") as f:
    API_KEY = f.read().strip()

# APIエンドポイント
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

# 川柳の例（46で生成されたものをここに入れる）
senryu_list = [
    "麦わら帽 照り返しさえ 味方だね",
    "風鈴の 音色涼やか 昼下がり",
    "入道雲 未来語るかの ごとく湧く",
    "花火散り 刹那の光 焼き付ける",
    "ラムネ瓶 ビー玉追いかけ 夏休み",
    "夕立後 アスファルトの匂い立つ",
    "かき氷 頭キンキン 夏の味",
    "浴衣着て 下駄の音響く 夏祭り",
    "線香花火 儚い光 見つめてる",
    "蝉の声 うるさき夏を 知らせてる"
]

# 評価プロンプトの作成
prompt = "次の10個の川柳について、それぞれの『面白さ』を10点満点で評価し、理由も簡潔に添えてください。\n\n"
for i, s in enumerate(senryu_list, 1):
    prompt += f"{i}. {s}\n"
prompt += "\n出力形式は次のようにしてください：\n1. 評価: 8/10 理由: ○○○○○"

# JSONデータ
data = {
    "contents": [
        {
            "parts": [
                {
                    "text": prompt
                }
            ]
        }
    ]
}

headers = {
    "Content-Type": "application/json"
}

# APIリクエスト送信
response = requests.post(url, headers=headers, data=json.dumps(data))

# 結果の処理
if response.status_code == 200:
    result = response.json()
    output = result["candidates"][0]["content"]["parts"][0]["text"]
    print("川柳の評価:\n")
    print(output)
else:
    print(f"エラー: {response.status_code}")
    print(response.text)