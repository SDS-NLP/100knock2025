# 適当なお題を設定し、川柳の案を10個作成せよ。

from google import genai
import os
from dotenv import load_dotenv
from pathlib import Path

def generate_ai_response(prompt):
    # itsukihidakaディレクトリの.envファイルを読み込む
    env_path = Path(__file__).parent.parent / '.env'
    load_dotenv(env_path)

    # 環境変数からAPIキーを取得
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("環境変数 GOOGLE_API_KEY が設定されていません。")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

prompt = """以下のお題で川柳を10個作成してください。
お題：「現代社会の悩み」

ルール：
1. 5・7・5の17音で作成すること
2. 現代社会の様々な悩みや問題をテーマにすること
3. ユーモアのある表現を心がけること
4. 10個の川柳を作成すること"""

answer = generate_ai_response(prompt)
print(answer)

