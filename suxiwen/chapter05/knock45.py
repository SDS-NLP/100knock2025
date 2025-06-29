import os
import requests
from dotenv import load_dotenv

# 環境変数からAPIキーを読み込む
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
api_url ="https://api.groq.com/openai/v1/chat/completions"
# マルチターン対話の履歴（messages）を用意
messages = [
    {
        "role": "user",
        "content": "つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。"
    },
    {
        "role": "assistant",
        "content": "目的地は自由が丘の1つ隣の各駅停車駅である「緑が丘駅」です。"
    },
    {
        "role": "user",
        "content": "さらに、つばめちゃんが自由が丘駅で乗り換えたとき、先ほどとは反対方向の急行電車に間違って乗車してしまった場合を考えます。目的地の駅に向かうため、自由が丘の次の急行停車駅で降車した後、反対方向の各駅停車に乗車した場合、何駅先の駅で降りれば良いでしょうか？"
    }
]

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

payload = {
    "model": "meta-llama/llama-4-scout-17b-16e-instruct",
    "messages": [{"role": "user", "content": messages[-1]["content"]}],
    "temperature": 0.0
}



response = requests.post(api_url, headers=headers, json=payload)

# 応答出力

result = response.json()
output = result["choices"][0]["message"]["content"]
print("モデルの回答:", output)