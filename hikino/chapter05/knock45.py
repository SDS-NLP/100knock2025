import anthropic

with open("../../../claude_apikey.txt", mode = "r") as f:
  key = f.read()
client = anthropic.Anthropic(api_key = key)

messages = [
    {"role": "user",   "content": """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
    東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。
    自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。
    目的地の駅の名前を答えてください。"""},
    {"role": "assistant", "content": """自由が丘から大井町方面に向かう急行の停車駅は以下の通り：
    自由が丘 → 大岡山 → 旗の台 → 中延 → 大井町つまり、自由が丘の次の急行停車駅は「大岡山」です。
    「大岡山」の1つ手前（=自由が丘方面の隣駅）は「緑が丘」です。
    よって、つばめちゃんの目的地は緑ヶ丘駅です。
    """},
    {"role": "user",   "content": """さらに、つばめちゃんが自由が丘駅で乗り換えたとき、
    先ほどとは反対方向の急行電車に間違って乗車してしまった場合を考えます。
    目的地の駅に向かうため、自由が丘の次の急行停車駅で降車した後、
    反対方向の各駅停車に乗車した場合、何駅先の駅で降りれば良いでしょうか？"""}
]

response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=messages
)

print(response.content[0].text)