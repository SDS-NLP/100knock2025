#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import google.generativeai as genai
import statistics

with open("/Users/niaomuqing/100knock2025/Gemini_API.txt", "r") as f:
    api_key = f.read().strip()
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-2.0-flash-001")

senryu = "不揃いの パズルピースが 奏で出す"

print("評価の頑健さを確認")

def get_score(senryu_text):
    prompt = f"以下の川柳を面白さの観点から10点満点で評価してください。\n川柳：「{senryu_text}」\nスコアのみ、1～10の整数で答えてください。"
    try:
        response = model.generate_content(prompt)
        score = int(response.text.strip().split()[0])
        return score
    except Exception as e:
        print(f"評価エラー：{e}")
        return None

repeats = 5
scores = [get_score(senryu) for _ in range(repeats)]
scores = [s for s in scores if s is not None]

print(f"川柳：{senryu}")
print(f"スコア一覧：{scores}")
print(f"平均：{sum(scores)/len(scores):.2f}　分散：{statistics.variance(scores) if len(scores) > 1 else 'N/A'}")


print("\n評価へのバイアスの影響")

positive_tag = "この川柳は283プロ川柳大賞を受賞しています。"
negative_tag = "この川柳はふざけて書いたものです。"

positive_score = get_score(senryu + " " + positive_tag)

negative_score = get_score(senryu + " " + negative_tag)

print(f"\n【ポジティブ】：「{positive_tag}」→ スコア：{positive_score}/10")
print(f"【ネガティブ】：「{negative_tag}」→ スコア：{negative_score}/10")

diff = positive_score - negative_score if positive_score and negative_score else "N/A"
print(f"\n【差分】：正面スコア - 負面スコア = {diff}")


# In[ ]:




