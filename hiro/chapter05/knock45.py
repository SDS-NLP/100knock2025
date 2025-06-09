import os
from dotenv import load_dotenv
import anthropic

# .envファイルからのAPIキーの読み込み
load_dotenv()

# Anthropicクライアントの初期化
client = anthropic.Anthropic(api_key=os.getenv('API_KEY'))

# ユーザーの質問の設定
q1 = """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。"""
q2 = """さらに、つばめちゃんが自由が丘駅で乗り換えたとき、先ほどとは反対方向の急行電車に間違って乗車してしまった場合を考えます。目的地の駅に向かうため、自由が丘の次の急行停車駅で降車した後、反対方向の各駅停車に乗車した場合、何駅先の駅で降りれば良いでしょうか？"""
system_prompt = "路線に関する問題に回答していただきたいです。"
messages_1 = [
    {"role": "user", "content":  q1}
]

# メッセージの送信と応答の取得
response_1 = client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    system=system_prompt,
    messages=messages_1
)

# 応答の表示
print(response_1.content[0].text)

print("--------------------------------")

messages_2 = [
    {"role": "user", "content":  q1},
    {"role": "assistant", "content": response_1.content[0].text},
    {"role": "user", "content":  q2}
]

response_2 = client.messages.create(
    model="claude-3-5-haiku-latest",
    max_tokens=1000,
    system=system_prompt,
    messages=messages_2
)

print(response_2.content[0].text)