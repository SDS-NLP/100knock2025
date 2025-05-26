import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env から API キーを読み込み
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Gemini Flash API を初期化
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# --- 問題46: 川柳生成 ---

# 任意のお題
topic = "サラリーマン"

# 川柳生成プロンプト
senryu_prompt = f"""
お題「{topic}」で川柳を10個作成してください。
季語や厳密な俳句ルールは不要で、5-7-5のリズムを意識したユーモラスな川柳にしてください。
出力は1行1句、合計10句でお願いします。
"""

senryu_response = model.generate_content(senryu_prompt)
senryu_list = [line.strip() for line in senryu_response.text.strip().splitlines() if line.strip()]

print("【生成された川柳】")
for i, s in enumerate(senryu_list, 1):
    print(f"{i}. {s}")

# --- 問題47: LLMによる評価 ---

# 評価プロンプト
eval_prompt = "以下の川柳をユーモアや創造性の観点から10点満点で評価してください。\n\n"

for i, s in enumerate(senryu_list, 1):
    eval_prompt += f"{i}. {s}\n"

eval_prompt += "\n各川柳について、「番号. 評価点（1〜10）」の形式で出力してください。"

eval_response = model.generate_content(eval_prompt)

print("\n【川柳の評価（面白さ）】")
print(eval_response.text.strip())
