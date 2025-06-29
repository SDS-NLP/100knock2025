#!/usr/bin/env python
# coding: utf-8

# In[2]:


prompt = """アイドルマスターシャイニーカラーズの新(?)ユニット「コメティック」を題に川柳の案を10個作成してください"""

import google.generativeai as genai

with open("/Users/niaomuqing/100knock2025/Gemini_API.txt", "r") as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")

response = model.generate_content(prompt)
answer = response.text.strip()

print(answer)

