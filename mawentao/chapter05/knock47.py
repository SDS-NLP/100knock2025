#!/usr/bin/env python
# coding: utf-8

# In[2]:


import google.generativeai as genai

# APIキー読み込み
with open("/Users/niaomuqing/100knock2025/Gemini_API.txt", "r") as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash-001")

# prompt：生成 + 評価を一度に行う
prompt = """
アイドルマスターシャイニーカラーズの新ユニット「コメティック」を題に、以下の形式で川柳を10個作成し、それぞれに対して面白さを10点満点で評価してください。

出力形式：
1. 川柳
   評価：◯点

2. 川柳
   評価：◯点

面白さの点数（1～10）を数字のみで答えてください。
"""

response = model.generate_content(prompt)
print(response.text.strip())


# In[ ]:




