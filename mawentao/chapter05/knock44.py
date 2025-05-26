#!/usr/bin/env python
# coding: utf-8

# In[1]:


prompt = """つばめちゃんは渋谷駅から東急東横線に乗り、自由が丘駅で乗り換えました。
東急大井町線の大井町方面の電車に乗り換えたとき、各駅停車に乗車すべきところ、間違えて急行に乗車してしまったことに気付きました。
自由が丘の次の急行停車駅で降車し、反対方向の電車で一駅戻った駅がつばめちゃんの目的地でした。
目的地の駅の名前を答えてください。駅名だけを1語で出力してください。"""

import google.generativeai as genai

with open("/Users/niaomuqing/100knock2025/Gemini_API.txt", "r") as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")

response = model.generate_content(prompt)
answer = response.text.strip()

print(f"モデルの出力：{answer}")


# In[ ]:




