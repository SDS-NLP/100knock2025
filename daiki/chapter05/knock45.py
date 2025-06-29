import requests
import json

# APIキー読み込み
with open("/Users/aa/100knock2025/daiki/chapter05/gemini_apikey.txt", "r") as f:
    API_KEY = f.read().strip()

# エンドポイント
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"
headers = {"Content-Type": "application/json"}

# プロンプト（つばめちゃん問題）
prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。さらに、つばめちゃんが自由が丘駅で乗り換えたとき、先ほどとは反対方向の急行電車に間違って乗車してしまった場合を考えます。目的地の駅に向かうため、自由が丘の次の急行停車駅で降車した後、反対方向の各駅停車に乗車した場合、何駅先の駅で降りれば良いでしょうか？

"""

# リクエストボディ
data = {
    "contents": [
        {
            "parts": [
                {"text": prompt}
            ]
        }
    ]
}

# リクエスト送信
response = requests.post(url, headers=headers, json=data)

# 結果表示
if response.status_code == 200:
    res = response.json()
    reply = res["candidates"][0]["content"]["parts"][0]["text"]
    print("Geminiの応答：")
    print(reply.strip())
else:
    print("APIエラー:")
    print(response.status_code)
    print(response.text)
