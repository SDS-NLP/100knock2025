import requests
from dotenv import load_dotenv
import os
from knock46 import output

senryu_list = [line.strip("・0123456789. ") for line in output.split("\n") if line.strip()]
senryu_list = [s for s in senryu_list if s != ""][:10]  # 上位10個に制限


load_dotenv()  # .envファイルを読み込む
API_KEY = os.getenv("GROQ_API_KEY")
# Groq API情報
API_URL = "https://api.groq.com/openai/v1/chat/completions"

# プロンプト（Zero-Shot）
prompt = "以下の川柳それぞれについて、10点満点で面白さを評価してください。\n"
for i, s in enumerate(senryu_list, 1):
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
