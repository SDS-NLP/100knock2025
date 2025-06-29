import pandas as pd
import os
from dotenv import load_dotenv
import anthropic

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv('API_KEY'))

script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "college_computer_science.csv")

df = pd.read_csv(csv_path, header = None)
n = 0

for i in range(len(df)):
  question = df.loc[i,0]
  A = df.loc[i,1]
  B = df.loc[i,2]
  C = df.loc[i,3]
  D = df.loc[i,4]
  
  system_prompt = "あなたは大学のコンピュータサイエンスの専門家です。与えられた問題に対して、最も適切な選択肢を1つ選択してください。回答は選択肢の記号（A、B、C、D）のみを「回答: X」の形式で返してください。"
  messages = [
    {"role": "system", "content": "あなたは大学のコンピュータサイエンスの専門家です。与えられた問題に対して、最も適切な選択肢を1つ選択してください。回答は選択肢の記号（A、B、C、D）のみを「回答: X」の形式で返してください。"},
    {"role": "user", "content": f"""問題: {question}

選択肢:
A: {A}
B: {B}
C: {C}
D: {D}

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
    model="claude-3-5-haiku-latest",
    max_tokens=1024,
    system=system_prompt,
    messages=messages
)
  res = response.content[0].text
  answer = res.replace("回答: ", "")
  right_answer = df.loc[i,5]
  if answer == right_answer:
    n += 1

ratio = n/len(df)
print(f"正答率: {ratio*100}%")