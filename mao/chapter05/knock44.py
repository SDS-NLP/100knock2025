"""
knock44:対話
以下の問いかけに対する応答を生成せよ。

つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、
間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、
反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。
"""

import os
from dotenv import load_dotenv
import google.generativeai as genai

# 環境変数の読み込みとクライアント設定
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# few-shot用プロンプトの構築
prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、
間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、
反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。
"""

response = model.generate_content(prompt)
print(response.text.strip())   #田園調布
