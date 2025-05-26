#42. 多肢選択問題の正解率
from google import genai
from dotenv import load_dotenv
import os
import pandas as pd
import time

load_dotenv()
key = os.getenv("API_KEY")

client = genai.Client(api_key=key)

#問題データの読み込み
df=pd.read_csv("japanese_idiom.csv",encoding="utf-8",header=None, names=["問題", "A", "B", "C", "D", "正解"])
labels = ["A", "B", "C", "D"]
correct_count = 0

for i, row in df.iterrows():
    question = row["問題"]
    choices = [row["A"],row["B"],row["C"],row["D"]]
    correct = row["正解"]

    choices_text = "\n".join([f"{label}. {choice}" for label, choice in zip(labels, choices)])
    prompt=f"""
問題: {question}
選択肢:
{choices_text}

正解をA-Dのアルファベットで答えてください。
ただし、解答の際はアルファベット１文字のみで答え、他の言葉を付け加えないようにしてください。
"""
    #print(prompt)
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    #print(response.text)
    answer=response.text
    print(f"Q{i+1}: モデルの回答: {answer} / 正解: {correct}")

    # 正誤判定
    if correct in answer:
        correct_count += 1

    time.sleep(5) #API利用制限に引っかかるので間隔をあけてスピードを遅くする→解答生成にめちゃくちゃ時間かかる、、、

accuracy = correct_count / len(df)
print(f"\n 正解率: {correct_count}/{len(df)} = {accuracy:.2%}")

##結果##
#  正解率: 144/150 = 96.00%