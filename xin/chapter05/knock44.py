import os
import requests
from dotenv import load_dotenv

# .envからAPIキーを読み込み
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
api_url ="https://api.groq.com/openai/v1/chat/completions"

# プロンプト（問 = """
prompt = """
線路図：'https://www.tokyu.co.jp/railway/station/map.html'
問題：つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。
自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。
"""

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [{"role": "user", "content": prompt}],
    "temperature": 0.0
}

response = requests.post(api_url, headers=headers, json=payload)

# 応答出力

result = response.json()
output = result["choices"][0]["message"]["content"]
print("モデルの回答:", output)

