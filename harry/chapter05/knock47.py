import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 課題1で生成した川柳（ここでは例として固定）
senryu_list = [
    "1.論文を　書かぬ罪業　積もりゆく",
    "2.指導室　扉の前で　深呼吸",
    "3.締切に　追われて逃げて　また捕まる",
    "4.学振を　夢見て消えた　夏の海",
    "5.深夜二時　誰かが光る　ラボの窓",
    "6.教授から　「面白いね」　怖すぎる",
    "7.データ消え　エクセルの海　ただ茫然",
    "8.図書館の　隅が今日から　我が家です",
    "9.学会で　旅費は出ない　でも行くよ",
    "10.修了と　同時にくるのは　燃え尽き感"
]

# 評価を依頼するプロンプト
senryu_text = "\n".join(senryu_list)
prompt = f"""
以下の川柳10句を、それぞれ面白さの観点から10点満点で評価してください。
出力形式は「1. 8点」のように番号と得点を対応させてください。

{senryu_text}
"""

payload = {
    "model": MODEL,
    "temperature": 0,  # 安定した評価
    "messages": [
        {"role": "system", "content": "あなたはユーモアに厳しい日本の川柳評論家です。各句の面白さを的確に採点してください。"},
        {"role": "user", "content": prompt}
    ]
}

response = requests.post(API_URL, headers=headers, json=payload)

if response.status_code == 200:
    evaluation = response.json()["choices"][0]["message"]["content"].strip()
    print("\n📊 川柳の評価:")
    print(evaluation)
    with open("senryu_evaluation.txt", "w", encoding="utf-8") as f:
        f.write(evaluation)
else:
    print("❌ APIエラー:", response.status_code, response.text)