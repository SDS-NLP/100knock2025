import os
from dotenv import load_dotenv
import google.generativeai as genai

# .envファイルからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# 使用モデル（制限に余裕のあるモデル推奨）
model = genai.GenerativeModel("models/gemini-1.5-flash")

# knock46で生成された川柳（手動で貼り付けてください）
senryu_list = [
    "AIが描く　未来の絵は　まだ白紙"
    "知恵の泉　AI深く　潜りゆく"
    "便利なAI　人の仕事は　どうなるやら"
    "AI先生　優しく教えて　未来へ導く"
    "冷たい画面　AIの言葉　心に響く"
    "夢を語る　AIと共に　夜空見上げる"
    "進化続ける　AIの瞳　光放つ"
    "創造の翼　AI広げ　空を飛ぶ"
    "頼りになる　AIのパートナー　共に生きる"
    "答えは一つ　AIは言う　その先へは"
]

# プロンプト構築（10段階で各句を評価）
senryu_text = "\n".join([f"{i+1}. {s}" for i, s in enumerate(senryu_list)])
prompt = f"""
以下の川柳を、面白さの観点からそれぞれ10段階で評価してください。1が最低、10が最高とします。
各句について、短くてよいので理由も添えてください。

{senryu_text}

出力形式：
1. 評価: 8 理由: 〜〜〜
2. 評価: 7 理由: 〜〜〜
...
"""

# モデルにプロンプトを送信
response = model.generate_content(prompt)

# 結果を表示
print("📘 川柳評価（10段階）:")
print(response.text.strip())
