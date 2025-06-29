import requests
import os
import re
import pandas as pd
from dotenv import load_dotenv

# API準備
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"
HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# 川柳10句（評価対象）
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

# プロンプトベース
senryu_text = "\n".join(senryu_list)
prompt = f"""
以下の川柳10句を、それぞれ面白さの観点から10点満点で評価してください。
出力形式は「1. 8点」のように番号と得点を対応させてください。

{senryu_text}
"""

# 評価回数
NUM_TRIALS = 5
scores = {str(i): [] for i in range(1, 11)}

def get_scores():
    payload = {
        "model": MODEL,
        "temperature": 1.0,
        "messages": [
            {"role": "system", "content": "あなたはユーモアに厳しい日本の川柳評論家です。各句の面白さを10点満点で評価してください。"},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload)

    if response.status_code == 200:
        result = response.json()["choices"][0]["message"]["content"]
        lines = result.strip().split("\n")
        for line in lines:
            match = re.match(r"(\d+)[\.\s]*([0-9]{1,2})点", line)
            if match:
                idx, score = match.group(1), int(match.group(2))
                if idx in scores:
                    scores[idx].append(score)
    else:
        print("❌ APIエラー:", response.status_code, response.text)

# 評価を複数回実行
for trial in range(NUM_TRIALS):
    print(f"📊 評価実行 {trial + 1}/{NUM_TRIALS} ...")
    get_scores()

# DataFrame化して分散・平均を計算
df = pd.DataFrame(scores, index=[f"Trial{i+1}" for i in range(NUM_TRIALS)]).T
df["平均"] = df.mean(axis=1)
df["標準偏差"] = df.std(axis=1).round(2)
df.index.name = "川柳番号"

print("\n🎯 評価結果（平均と標準偏差）:")
print(df[["平均", "標準偏差"]])

# 結果を保存
df.to_csv("senryu_variance.csv", encoding="utf-8-sig")
print("\n✅ 結果を senryu_variance.csv に保存しました。")