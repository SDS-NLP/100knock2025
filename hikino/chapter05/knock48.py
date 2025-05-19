from google import genai

with open("../../../gemini_apikey.txt", mode = "r") as f:
    key = f.read()
client = genai.Client(api_key = key)

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents=f"""{text}にあるそれぞれの川柳について、1から10で評価をつけてください。
    テーマは好不景気や流行語など、その年の流行や世相を反映しながら、
    サラリーマンの悲哀をユーモラスに詠む、サラリーマン川柳です。"""
)

print(response.text)