import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
API_KEY = os.getenv("API_KEY")

# ここは変更なし
genai.configure(api_key=API_KEY)

# モデル名を v1beta 対応のものに
model = genai.GenerativeModel("gemini-2.0-flash")

prompt = """
以下の歴史的できごとを、9世紀に関係するものとして、年代の古い順に並び替えてください。
解説や根拠は不要で、順番（例：イ→ウ→ア）のみを出力してください。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。
"""

response = model.generate_content(prompt)
print("回答（年代順）:", response.text.strip())
