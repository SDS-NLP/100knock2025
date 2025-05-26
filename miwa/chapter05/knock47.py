#47. LLMによる評価
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")

client = genai.Client(api_key=key)

prompt = """
次の10個の川柳の面白さを1から10の十段階で評価してください。

1.  鉄路の風　夢を乗せゆく　白い鳥
2.  弁当と　車窓の景色　旅気分
3.  故郷へ　時を縮めて　会いに行く
4.  ビジネスマン　一息ついて　また仕事
5.  新幹線　日本の動脈　今日も走る
6.  速すぎて　景色が流れる　夏の空
7.  揺れもなく　快適すぎる　時の旅
8.  駅弁の　匂いと音と　旅の味
9.  トンネルを　抜ければ広がる　雪景色
10. 新幹線　技術の粋を　未来へつなぐ

"""

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt, 
    config=types.GenerateContentConfig(
    max_output_tokens=1000,
    temperature=0.1) )
print(response.text)