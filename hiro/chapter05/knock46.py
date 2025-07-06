import os
from dotenv import load_dotenv
from google import genai
import random
from google.genai.types import GenerateContentConfig

load_dotenv()

client = genai.Client(api_key=os.getenv('GOOGLE_API_KEY'))

# 適当なお題リスト
topics = [
    "プログラミング",
    "コーヒー",
    "雨の日",
    "通勤電車",
    "リモートワーク",
    "スマートフォン",
    "猫",
    "お正月",
    "桜",
    "夏祭り"
]

# ランダムにお題を選択
selected_topic = random.choice(topics)
print(f"お題: {selected_topic}")
print("=" * 30)

# 川柳を10個作成するプロンプト
prompt = f"""
お題「{selected_topic}」で川柳を10個作成してください。
各川柳には番号を付けて、以下の形式で出力してください：

1. ○○○○○（5音）
   ○○○○○○○（7音）
   ○○○○○（5音）

2. ○○○○○（5音）
   ○○○○○○○（7音）
   ○○○○○（5音）

...（10個まで）

ユーモアや風刺を込めた川柳を作成してください。
"""

# システム指示を設定
config = GenerateContentConfig(
    system_instruction=[
        "あなたは経験豊かな俳句・川柳の専門家です。",
        "5-7-5の音律（語数ではない）を正確に守り、季語や心情を巧みに表現する才能があります。",
        "日本の伝統的な川柳の技法を理解し、現代的な感性も取り入れることができます。",
        "ユーモアや風刺、人生の機微を短い言葉で表現することが得意です。",
        "音数を正確に数え、美しい日本語で川柳を作成してください。"
    ]
)

response = client.models.generate_content(
    model="gemini-2.5-flash-preview-05-20",
    contents=prompt,
    config=config
)

print(response.text)