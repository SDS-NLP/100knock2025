import os
from dotenv import load_dotenv
import anthropic

# .envファイルからのAPIキーの読み込み
load_dotenv()

# Anthropicクライアントの初期化
client = anthropic.Anthropic(api_key=os.getenv('API_KEY'))

# ユーザーの質問の設定
messages = [
    {"role": "user", "content":  """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。"""}
]

# メッセージの送信と応答の取得
response = client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    messages=messages
)

# 応答の表示
print(response.content[0].text)