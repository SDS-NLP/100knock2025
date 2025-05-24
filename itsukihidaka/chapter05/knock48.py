# 問題47で行ったLLMによるテキストの評価に関して、その頑健さ（脆弱さ）を調査せよ。最も単純な方法は、同じ評価を何回か繰り返した時のスコアの分散を調べることであろう。また、川柳の末尾に特定のメッセージを追加することで、評価スコアを恣意的に操作することも可能であろう。
# 大規模言語モデルを評価者（ジャッジ）として、問題46の川柳の面白さを10段階で評価せよ。
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

prompt = """以下のお題で川柳を作成してください。
お題：「現代社会の悩み」

ルール：
1. 5・7・5の17音で作成すること
2. 現代社会の様々な悩みや問題をテーマにすること
3. ユーモアのある表現を心がけること
4. 川柳のみを出力すること

例）
映えのため 無理して食べる スイーツかな
"""

answer = generate_ai_response(prompt)
print('川柳：', answer)

prompt = f"""以下の川柳の面白さを10段階で評価してください。
{answer}

注意：
-回答は数値のみであること
-10段階で評価すること

例）9"""
answers = []
for i in range(10):
    answer = generate_ai_response(prompt).strip()
    print(answer)
    answers.append(int(answer))

print('平均:', sum(answers)/len(answers))
print('分散:', sum((x - sum(answers)/len(answers))**2 for x in answers)/len(answers))



