#23. セクション構造
import json
import re
import collections

path="jawiki-country.json"

uk_text=None
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        article=json.loads(line)
        if article["title"]=="イギリス":
            uk_text = article["text"]
            break

pattern=r"={2,}.*?={2,}"
result = re.findall(pattern, uk_text)
section={}
for text in result:
    c1 = collections.Counter(text) #text内の文字の出現回数を数える
    c2 = int(c1["="]/2) #text内の=の数÷２
    text = text.replace("=", "")
    section[text] = c2 -1

print(section)