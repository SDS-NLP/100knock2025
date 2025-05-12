#24. ファイル参照の抽出
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

pattern=r"\[\[ファイル:(.*?)(?:\||\])" #|でそのあとに画像の情報が続いているものと、そのまま]]で終わっているものがある。
result = re.findall(pattern, uk_text)
print(result)