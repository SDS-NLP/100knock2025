#26. 強調マークアップの除去
import json
import re
path="jawiki-country.json"

uk_text=None
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        article=json.loads(line)
        if article["title"]=="イギリス":
            uk_text = article["text"]
            break

#基礎情報テンプレート全体を抽出
pattern=r"\{\{基礎情報.*?\n(.*?)\n\}\}" 
result1 = re.findall(pattern, uk_text,re.DOTALL)
#print(result)

#フィールド名と値を抽出
pattern=r"\|(.*?)\s*=\s*(.*?)(?=\n\|)" 
result1[0] += "\n|" #最後の項目の後ろを他の項目と同じにする
result2 = re.findall(pattern, result1[0], re.DOTALL)
information= {}
for i,j in result2:
    information[i] = j

#強調マークアップ除去
for k, v in information.items():
    information[k]=re.sub(r"\'{2,5}", "", v)
    print(f'{k} : {information[k]}')
