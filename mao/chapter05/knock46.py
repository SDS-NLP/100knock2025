"""
knock46:川柳の生成
適当なお題を設定し、川柳の案を10個作成せよ。
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

# 環境変数の読み込みとクライアント設定
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# プロンプトの構築
prompt = """
第一生命が主催するサラリーマン川柳コンテストに出す川柳を10個提案してください。
"""

response = model.generate_content(prompt)
print(response.text.strip())  
"""
1. 残業代 雀の涙じゃ 足りないよ
2. プレッシャー 胃が痛いよ 週末まで
3. 社内恋愛 噂の的 ドキドキする
4. 年末調整 計算複雑 頭痛い
5. 部署移動 新しい顔 緊張する
6. 無駄会議 時間だけが 過ぎてゆく
7. 昇給発表 期待はずれ ため息つく
8. オンライン会議 猫が邪魔 画面乱れ
9. 昼休み時間 短いけど 幸せ時間
10. 定年退職 第二の人生 ワクワクする
"""
