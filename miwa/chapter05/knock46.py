#46. 川柳の生成
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
key = os.getenv("API_KEY")

client = genai.Client(api_key=key)

prompt = """「新幹線」をお題として、川柳の案を１０個考えてください。
"""

response = client.models.generate_content(
    model="gemini-2.0-flash", contents=prompt, 
    config=types.GenerateContentConfig(
    max_output_tokens=500,
    temperature=0.9) )
print(response.text)