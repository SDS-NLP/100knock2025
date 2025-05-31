import openai

with open("key.txt", "r") as file:
    api_key = file.read().strip()

client = openai.OpenAI(
    api_key=api_key,  # 読み込んだAPIキーをここに使います
    base_url="https://api.groq.com/openai/v1"  # Groq専用のURLを指定します
)

# LLMに聞きたい内容
question = """
次の三つの出来事（ア〜ウ）を、年代の古い順に並べてください。

ア: 藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ: 嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ: 藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。

ラベル（ア・イ・ウ）だけで順番を答えてください。
"""

# モデルに質問を送って、応答を受け取ります
response = client.chat.completions.create(
    model="meta-llama/llama-4-scout-17b-16e-instruct",  # 使用するGroqのモデル名
    messages=[
        {"role": "user", "content": question}  # ユーザーとして質問を送る
    ],
    temperature=0.3  # 出力の「ランダムさ」を調整（0に近いほど堅実な答え）
)

# 応答の中から実際の答えの部分を取り出して表示します
print(response.choices[0].message.content)
