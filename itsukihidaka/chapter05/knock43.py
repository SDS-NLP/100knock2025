import pandas as pd
from google import genai
from google.genai import types
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
        model="gemini-2.0-flash", contents=prompt,     
        config=types.GenerateContentConfig(
        temperature=0)
    )
    return response.text


df = pd.read_csv('itsukihidaka/chapter05/high_school_mathematics.csv', header=None, names=['問題文', 'A', 'B', 'C', 'D', '正解'])
# 正解がD以外の場合、その選択肢をDに変換
for i in range(len(df)):
    if df.loc[i, '正解'] != 'D':
        # 正解の選択肢を取得
        correct_choice = df.loc[i, '正解']
        # 正解の選択肢の値を取得
        correct_value = df.loc[i, correct_choice]
        d_value = df.loc[i, 'D']
        # Dの値を正解の選択肢の値に変更
        df.loc[i, 'D'] = correct_value
        # 正解の選択肢をDに変更
        df.loc[i, correct_choice] = d_value
        # 正解をDに変更
        df.loc[i, '正解'] = 'D'

collect_answer = 0
n = df.shape[0]

for _, row in df.iterrows():
    prompt = f"問題文: {row['問題文']}\n選択肢\nA: {row['A']}\nB: {row['B']}\nC: {row['C']}\nD: {row['D']} \n回答は選択肢番号のみで答えよ \n例：B"

    answer = generate_ai_response(prompt).strip()
    print('gemini:', answer)
    print('正解:', row['正解'])
    if answer == row['正解']:
        collect_answer += 1

print(collect_answer/n)
#0.54







