import os
import google.generativeai as genai
from dotenv import load_dotenv

# .envファイルからAPIキーを読み込む
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Gemini APIの初期化
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")

# 問題文
prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、
間違えて急行に乗車してしまったことに気付きました。
自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。
目的地の駅の名前を答えてください。
"""

# 回答の取得
response = model.generate_content(prompt)
print("つばめちゃんの目的地：", response.text.strip())
