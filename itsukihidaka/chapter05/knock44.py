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

question = """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。"""

answer = generate_ai_response(question)
print(answer)
