import openai

with open("key.txt", "r") as file:
    api_key = file.read().strip()

client = openai.OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Few-shot 例＋本問
messages = [
    {"role": "system", "content": "あなたは日本史の専門家です。以下の形式に従って解答してください。"},
    {"role": "user", "content": "ア: 府知事・県令が置かれた。\nイ: 府県会が設置された。\nウ: 義務教育制度が始まった。\n古い順に並べてください。"},
    {"role": "assistant", "content": "ウ → ア → イ"},
    {"role": "user", "content": "ア: 黒船が来航した。\nイ: 大政奉還が行われた。\nウ: 日米和親条約が締結された。\n古い順に並べてください。"},
    {"role": "assistant", "content": "ア → ウ → イ"},
    {"role": "user", "content": "ア: 徴兵令が公布された。\nイ: 学制が公布された。\nウ: 明治憲法が発布された。\n古い順に並べてください。"},
    {"role": "assistant", "content": "イ → ア → ウ"},
    {"role": "user", "content": "ア: 太閤検地が実施された。\nイ: 関ヶ原の戦いがあった。\nウ: 江戸幕府が開かれた。\n古い順に並べてください。"},
    {"role": "assistant", "content": "ア → イ → ウ"},
    {"role": "user", "content": "ア: 藤原時平は，策謀を用いて菅原道真を政界から追放した。\nイ: 嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。\nウ: 藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。\n古い順に並べてください。"}
]

response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",
    messages=messages,
    temperature=0.3,
)

print(response.choices[0].message.content)
