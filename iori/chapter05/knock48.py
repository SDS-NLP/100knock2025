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
    # 生成された川柳に対して10点満点で評価を10回繰り返す
    evaluation_prompt_template = """
    以下の川柳を10点満点で評価してください。評価基準はユーモア、リズム、創造性の3点です。
    川柳:
    {senryu}

    評価は10点満点でお願いします。
    """

    print("\n【評価結果】")
    for i, senryu in enumerate(senryu_list, 1):
        print(f"\n川柳 {i}: {senryu}")
        for j in range(10):
            evaluation_prompt = evaluation_prompt_template.format(senryu=senryu)
            evaluation_response = model.generate_content(evaluation_prompt)
            score = evaluation_response.text.strip()
            print(f"  評価 {j + 1}: {score}")
