import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# 安定版（おすすめ）
model = genai.GenerativeModel("gemini-1.5-flash")

prompt = """
9世紀に活躍した人物に関係する次のア～ウの出来事を、年代の古い順に正しく並べてください。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。

並び替えた順序だけを「イ→ウ→ア」のように答えてください。
"""

response = model.generate_content(prompt)
print(response.text)

# 出力：イ→ウ→ア