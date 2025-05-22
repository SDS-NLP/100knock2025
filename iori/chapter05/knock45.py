import os
import google.generativeai as genai
from dotenv import load_dotenv

# .envからAPIキーを読み込む
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Gemini設定
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat(history=[])

# 初回の問いかけ（文脈）
initial_prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、
間違えて急行に乗車してしまったことに気付きました。
自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。
目的地の駅の名前を答えてください。
"""

# 応答生成（1ターン目）
response1 = chat.send_message(initial_prompt)
print("最初の目的地の駅：", response1.text.strip())

# 追加の問いかけ（2ターン目）
followup_prompt = """
さらに、つばめちゃんが自由が丘駅で乗り換えたとき、先ほどとは反対方向の急行電車に間違って乗車してしまった場合を考えます。
目的地の駅に向かうため、自由が丘の次の急行停車駅で降車した後、反対方向の各駅停車に乗車した場合、
何駅先の駅で降りれば良いでしょうか？
"""

# 応答生成（2ターン目）
response2 = chat.send_message(followup_prompt)
print("戻るべき駅数：", response2.text.strip())
