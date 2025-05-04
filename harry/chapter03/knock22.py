import json
import re

# JSONファイルから記事を読み込む
with open('uk_article.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

text = data['text']

# 正規表現でカテゴリ名だけを抽出（非貪欲に）
category_matches = re.findall(r'\[\[Category:(.*?)(?:\|.*)?\]\]', text)

# 結果を表示
for category in category_matches:
    print(category)
