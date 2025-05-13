#21. カテゴリ名を含む行を抽出
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

pattern=r"\[\[Category:.*?\]\]"
result = re.findall(pattern, uk_text)
print(result)