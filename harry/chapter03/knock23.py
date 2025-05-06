import json
import re

# JSONファイルを読み込む
with open('uk_article.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

text = data['text']

# セクション見出しの抽出
section_pattern = re.compile(r'^(={2,})\s*(.+?)\s*\1$', re.MULTILINE)

# マッチしたセクション名とレベルを表示
for match in section_pattern.finditer(text):
    equal_signs = match.group(1)
    section_name = match.group(2)
    level = len(equal_signs) - 1  # == → 1, === → 2, etc.
    print(f'レベル {level} : {section_name}')
