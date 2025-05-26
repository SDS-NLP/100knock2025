"""
knock40:Zero-Shot推論
以下の問題の解答を作成せよ。ただし、解答生成はzero-shot推論とせよ。

9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。
ア：藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ：嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ：藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# APIキーの設定
genai.configure(api_key=api_key)

# モデルを明示的に指定（重要！）
model = genai.GenerativeModel(model_name="gemini-1.5-pro")

# プロンプト
prompt = """以下の問題の解答を作成せよ。ただし、解答生成はzero-shot推論とせよ。

9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア：藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ：嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ：藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。

回答は、選択肢の記号を順に並べて出力せよ。たとえば「イウア」などの形式で出力せよ。
"""

# 推論を実行
response = model.generate_content(prompt)

# 結果を表示
print("推論された順序:", response.text.strip())
