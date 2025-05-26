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

question = """9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア　藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ　嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ　藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。"""

answer = generate_ai_response(question)
print(answer)
