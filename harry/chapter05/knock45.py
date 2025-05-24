import requests
import os
from dotenv import load_dotenv

# APIキーの読み込み
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")
API_URL = "https://api.groq.com/openai/v1/chat/completions"
MODEL = "meta-llama/llama-4-scout-17b-16e-instruct"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}

# Step1の質問
q1 = """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、
間違えて急行に乗車してしまったことに気付きました。
自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。
目的地の駅の名前を答えてください。"""

# Step2の質問
q2 = """さらに、つばめちゃんが自由が丘駅で乗り換えたとき、
先ほどとは反対方向の急行電車に間違って乗車してしまった場合を考えます。
目的地の駅に向かうため、自由が丘の次の急行停車駅で降車した後、
反対方向の各駅停車に乗車した場合、何駅先の駅で降りれば良いでしょうか？"""

# ログファイルを準備
log_path = "dialogue_log.txt"
with open(log_path, "w", encoding="utf-8") as log_file:
    log_file.write("=== マルチターン対話ログ ===\n\n")
    log_file.write("🧑 Step 1:\n" + q1 + "\n")

# Step1: 初回の質問
payload1 = {
    "model": MODEL,
    "temperature": 0,
    "messages": [
        {"role": "system", "content": "あなたは鉄道に詳しい日本の案内係です。駅の順番や電車の種類に精通し、丁寧に推論して答えてください。"},
        {"role": "user", "content": q1}
    ]
}

response1 = requests.post(API_URL, headers=headers, json=payload1)

if response1.status_code == 200:
    answer1 = response1.json()["choices"][0]["message"]["content"].strip()
    print("🧠 Step 1 の応答:")
    print(answer1)
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write("\n🤖 Step 1 応答:\n" + answer1 + "\n")
else:
    print("❌ Step 1 APIエラー:", response1.status_code, response1.text)
    exit()

# Step2: その応答を踏まえた次の質問
payload2 = {
    "model": MODEL,
    "temperature": 0,
    "messages": [
        {"role": "system", "content": "あなたは鉄道に詳しい日本の案内係です。駅の順番や電車の種類に精通し、丁寧に推論して答えてください。"},
        {"role": "user", "content": q1},
        {"role": "assistant", "content": answer1},
        {"role": "user", "content": q2}
    ]
}

with open(log_path, "a", encoding="utf-8") as log_file:
    log_file.write("\n🧑 Step 2:\n" + q2 + "\n")

response2 = requests.post(API_URL, headers=headers, json=payload2)

if response2.status_code == 200:
    answer2 = response2.json()["choices"][0]["message"]["content"].strip()
    print("\n🧠 Step 2 の応答:")
    print(answer2)
    with open(log_path, "a", encoding="utf-8") as log_file:
        log_file.write("\n🤖 Step 2 応答:\n" + answer2 + "\n")
else:
    print("❌ Step 2 APIエラー:", response2.status_code, response2.text)