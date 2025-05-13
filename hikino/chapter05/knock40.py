import anthropic

with open("../../../claude_apikey.txt", mode = "r") as f:
  key = f.read()

client = anthropic.Anthropic(api_key = key)

messages = [
    {"role": "user",   "content": """9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。"""}
]

response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=messages
)

print(response.content[0].text)