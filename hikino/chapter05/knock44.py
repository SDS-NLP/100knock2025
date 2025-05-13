import anthropic

with open("../../../claude_apikey.txt", mode = "r") as f:
  key = f.read()
client = anthropic.Anthropic(api_key = key)

messages = [
    {"role": "user",   "content": """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
    東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。
    自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。
    目的地の駅の名前を答えてください。"""}
]

response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=messages
)

print(response.content[0].text)