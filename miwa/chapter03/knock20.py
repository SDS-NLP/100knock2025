#20. JSONデータの読み込み

path="jawiki-country.json"

import json

uk_text=None
with open(path, 'r', encoding='utf-8') as f:
    for line in f:
        article=json.loads(line)
        if article["title"]=="イギリス":
            uk_text = article["text"]
            break
    
print(uk_text)
