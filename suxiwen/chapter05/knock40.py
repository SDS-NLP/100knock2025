import requests
from dotenv import load_dotenv
import os
load_dotenv()  
API_KEY = os.getenv("GROQ_API_KEY")

API_URL = "https://api.groq.com/openai/v1/chat/completions"


prompt = """
以下の歴史上の出来事ア〜ウを、年代の古い順に並べてください。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。

回答は、「イ→ウ→ア」のように、日本語で順番のみを出力してください。
"""


headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.0
}

response = requests.post(API_URL, headers=headers, json=payload)


result = response.json()
output = result["choices"][0]["message"]["content"]
print("モデルの回答:", output)