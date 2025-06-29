import openai

with open("key.txt") as f:
    api_key = f.read().strip()

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

prompt = """「電車通学」をお題に、すべてひらがなで書かれた川柳を30個作ってください。
各川柳は3行構成で、1行目は5音、2行目は7音、3行目は5音で構成してください。
例：

あさのえき
つりかわにぎる 
ともだちと

つりかわを  
にぎってゆれる  
しんかんせん

このように、すべてひらがなで書いてください。
句点・カギカッコ・読点・記号は使わないでください。
川柳ごとに1行空けて、10句出力してください。
"""

response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=[{"role": "user", "content": prompt}],
    temperature=0.5
)

print(response.choices[0].message.content.strip())

def generate_senryu_list():
    return response.choices[0].message.content.strip().split("\n\n")