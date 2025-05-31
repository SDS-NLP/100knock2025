#40. Zero-Shot推論
from google import genai
from dotenv import load_dotenv
import os

# .envファイルを読み込む
load_dotenv()

# 環境変数からAPIキーを取得
key = os.getenv("API_KEY")

client = genai.Client(api_key=key)

question = """
9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。"""

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=question
)
print(response.text)