#44. 対話
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")

client = genai.Client(api_key=key)

prompt = """
つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。目的地の駅の名前を答えてください。
"""

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt, 
    config=types.GenerateContentConfig(
    max_output_tokens=1000,
    temperature=0.1) )
print(response.text)

##tempreture=0.1の回答
# つばめちゃんの目的地は**九品仏（くほんぶつ）駅**です。
# 
# 解説：
# 1.  **自由が丘駅の次の大井町線急行停車駅:** 自由が丘駅の次の大井町線急行停車駅は、二子玉川駅です。
# 2.  **二子玉川駅から一駅戻る:** 二子玉川駅から大井町方面に一駅戻ると、九品仏駅です。

## tempreture =0.9にしてみる
#つばめちゃんの目的地は九品仏（くほんぶつ）駅です。
# 
# 解説：
# 1.  自由が丘駅の次の東急大井町線の急行停車駅は、二子玉川駅です。
# 2.  二子玉川駅から大井町線で一駅戻ると、九品仏駅に着きます。

##大井町方面のを「」で強調したり、付け足しても、「自由が丘駅の東急大井町線、大井町方面の次の急行停車駅は、二子玉川駅です。」
# と答えられ、解答は九品仏駅となる。←なんで