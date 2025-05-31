#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import google.generativeai as genai

with open('/Users/niaomuqing/100knock2025/Gemini_API.txt', 'r', encoding='utf-8') as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

events = {
    "ア": "藤原時平は，策謀を用いて菅原道真を政界から追放した。",
    "イ": "嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。",
    "ウ": "藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。"
}

prompt = (
    "以下の三つの歴史的なできごとを、年代の古い順に並び替えてください。"
    "ただし、具体的な年代を調べるのではなく、文章の内容から自然言語的に推論してください。\n\n"
    f"ア：{events['ア']}\n"
    f"イ：{events['イ']}\n"
    f"ウ：{events['ウ']}\n\n"
    "並び替えた順序（記号のみで答えてください）："
)

model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")

response = model.generate_content(prompt)

print(response.text.strip())

