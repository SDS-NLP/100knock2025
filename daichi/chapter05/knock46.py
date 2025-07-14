import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# 使用モデル（制限の少ないモデルを使用）
model = genai.GenerativeModel("models/gemini-1.5-flash")

# 川柳生成プロンプト
prompt = """
以下のお題で川柳を10個作ってください。

お題：AI

※川柳はすべて5-7-5の形式にしてください。
"""

# モデルにプロンプトを送信
response = model.generate_content(prompt)

# 結果を表示
print("📘 川柳（お題：AI）:")
print(response.text.strip())
