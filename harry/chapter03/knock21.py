import json
import re

# JSONファイルから記事を読み込む
with open('uk_article.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

text = data['text']

# 行単位でループして、カテゴリを含む行を探す
for line in text.split('\n'):
    if re.search(r'\[\[Category:', line):
        print(line)
