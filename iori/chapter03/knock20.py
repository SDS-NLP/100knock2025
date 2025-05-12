
import json
import re

text_list = []
file_path = '/Users/iori/Documents/100knock2025/iori/chapter03/jawiki-country.json'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        text_list.append(json.loads(line))
for i in range(len(text_list)):
    if text_list[i]['title']=="イギリス":
        UK_text = str(text_list[i])
        break
#問題21-25用
#print(UK_text)
