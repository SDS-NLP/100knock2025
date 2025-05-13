import anthropic

with open("../../../claude_apikey.txt", mode = "r") as f:
  key = f.read()
client = anthropic.Anthropic(api_key = key)

messages = [
    {"role": "user",   "content": """あなたはユーモアのあるサラリーマンです。
    好不景気や流行語など、その年の流行や世相を反映しながら、
    サラリーマンの悲哀をユーモラスに詠む、
    サラリーマン川柳に応募するための川柳を10個詠んでください。"""}
]

response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    messages=messages
)

print(response.content[0].text)