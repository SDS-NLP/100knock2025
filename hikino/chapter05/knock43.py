import pandas as pd
import anthropic

with open("../../../claude_apikey.txt", mode = "r") as f:
  key = f.read()
client = anthropic.Anthropic(api_key = key)

df = pd.read_csv("../../../high_school_mathematics.csv", header = None)
n = 0

for i in range(len(df)):
  question = df.loc[i,0]
  A = df.loc[i,1]
  B = df.loc[i,2]
  C = df.loc[i,3]
  D = df.loc[i,4]
  messages = [
    {"role": "user", "content": "あなたは高校数学の専門家です。"},
    {"role": "user", "content": f"""{question}この問題に対して、A:{A},B:{B},C:{C},D:{D}の中から最も適切な選択肢を1つ選んでください。

回答は必ず以下の形式で、選択した記号1文字のみを返してください：
回答: [A/B/C/D]

注意:
- 理由説明、解説、思考過程は一切書かないでください
- 前置きや挨拶は書かないでください
- 選択肢の記号（A,B,C,D）のみを書いてください
- それ以外の文字や記号は一切含めないでください

例（正しい回答形式）:
回答: A

例（誤った回答形式）:
回答: Aだと思います
回答: この問題の答えはAです
回答: Aが正解です"""}
    ]
  
  response = client.messages.create(
    model="claude-3-5-haiku-20241022",
    max_tokens=1024,
    temperature=0.7,
    messages=messages
)
  res = response.content[0].text
  answer = res.replace("回答: ", "")
  right_answer = df.loc[i,5]
  print(answer)
  print(right_answer)
  if answer == right_answer:
    n = n + 1

print(n)
ratio = n/len(df)
print(ratio)

