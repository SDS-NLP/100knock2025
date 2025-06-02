#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import google.generativeai as genai

with open("/Users/niaomuqing/100knock2025/Gemini_API.txt", "r") as f:
    api_key = f.read().strip()

csv_path = "/Users/niaomuqing/100knock2025/professional_psychology.csv"

df = pd.read_csv("/Users/niaomuqing/100knock2025/professional_psychology.csv", header=None)
df.columns = ["question", "A", "B", "C", "D", "answer"]

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name="gemini-2.0-flash-001")

correct = 0
total = len(df)

for idx, row in df.iterrows():
    prompt = (
        f"問題：{row['question']}\n"
        f"A: {row['A']}\n"
        f"B: {row['B']}\n"
        f"C: {row['C']}\n"
        f"D: {row['D']}\n"
        "正解はどれですか？記号（A/B/C/D）のみで答えてください。"
    )

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip().upper()[0]
        df.loc[idx, "model_answer"] = answer
        df.loc[idx, "is_correct"] = (answer == row["answer"].strip().upper())
        if answer == row["answer"].strip().upper():
            correct += 1
    except Exception as e:
        print(f"第 {idx+1} エラー：{e}")
        df.loc[idx, "model_answer"] = "ERROR"
        df.loc[idx, "is_correct"] = False

accuracy = correct / total
print(f"正解率：{accuracy:.2%}（{correct}/{total}）")

