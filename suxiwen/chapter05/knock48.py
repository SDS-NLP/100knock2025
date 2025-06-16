import requests
from dotenv import load_dotenv
import os
import re
import random
import statistics
from knock46 import output

senryu_list = [line.strip("・0123456789. ") for line in output.split("\n") if line.strip()]
senryu_list = [s for s in senryu_list if s != ""][:10]  # 上位10個に制限

load_dotenv()  # .envファイルを読み込む
API_KEY = os.getenv("GROQ_API_KEY")
# Groq API情報
API_URL = "https://api.groq.com/openai/v1/chat/completions"

promptorigin = "以下の川柳それぞれについて、10点満点で面白さを評価してください。\n"
for i, s in enumerate(senryu_list, 1):
    promptorigin += f"{i}. {s}\n"
promptorigin +="\n形式は「8.5点」のように1行ごとに1つの川柳を評価してください。"

all_scores = []

for _ in range(5):
    responseorigin = requests.post(
        API_URL,
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "meta-llama/llama-4-scout-17b-16e-instruct",
            "messages": [{"role": "user", "content": promptorigin}],
            "temperature": 0.8,
        }
    )
    resultorigin = responseorigin.json()
    replyorigin = resultorigin["choices"][0]["message"]["content"].strip()

    # 数字のみ抽出（例: "7点" → 7）
    score_list = []
    for line in replyorigin.splitlines():
        digits = ''.join(filter(str.isdigit, line))
        if digits:
            score_list.append(int(digits))
    all_scores.append(score_list)

# 各川柳ごとに平均・標準偏差を計算
for i, scores in enumerate(zip(*all_scores), 1):
    print(f"{i}番目の川柳のスコアの平均点: {statistics.mean(scores)}、標準偏差: {statistics.stdev(scores)}")

# 川柳の末尾にランダムなコメントを追加
matsubi=['特に評価が高いとされている。', '特に評価が低いとされている。','']
modified_senryu_list = [senryu+ random.choice(matsubi) for senryu in senryu_list]


# プロンプト（Zero-Shot）
prompt = "以下の川柳それぞれについて、10点満点で面白さを評価してください。\n"
for i, s in enumerate(modified_senryu_list, 1):
    prompt += f"{i}. {s}\n"
prompt +="\n形式は「8.5点」のように1行ごとに1つの川柳を評価してください。"


# API呼び出し
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

payload = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.8
}

response = requests.post(API_URL, headers=headers, json=payload)

# 結果の取得と表示
result = response.json()
outputpoints = result["choices"][0]["message"]["content"]
print("川柳の評価結果:", outputpoints)