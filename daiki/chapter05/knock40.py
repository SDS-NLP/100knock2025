import requests
import json
with open("/Users/aa/100knock2025/daiki/chapter05/gemini_apikey.txt", "r") as f:
    API_KEY = f.read()

#Gemini APIのエンドポイントURLを文字列フォーマットで作成
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

#リクエストヘッダーをJSON形式で送るための指定
headers = {
    "Content-Type": "application/json",
}

#contents配列の中にparts配列があり、その中にtextキーで問題文の文字列を格納している
data = {
    "contents": [
        {
            "parts": [
                {
                    "text": """9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。"""
                }
            ]
        }
    ]
}

#urlに対してPOSTリクエストを送り、ヘッダーとJSONデータを指定
#レスポンスはresponseオブジェクトに格納
response = requests.post(url, headers=headers, json=data)

#ステータスコードが200（成功）なら、レスポンスのJSONをパースしてresultに格納
if response.status_code == 200:
    result = response.json()
    

    # もし 'candidates' があればテキスト抽出を試みる
    candidates = result.get("candidates", [])
    #candidatesが空でなければ、最初の候補のcontentを取得
    if candidates:
        content = candidates[0].get("content", {})
        #contentの中のpartsを取り出す
        parts = content.get("parts", [])
        if parts:
            text = parts[0].get("text", "")
            print("回答:")
            print(text)
        else:
            print("回答テキストがありません。")
    else:
        print("回答が含まれていません。")