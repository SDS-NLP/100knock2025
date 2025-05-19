# 記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ。

import json

def read_wiki_data():
    file_path = '/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter03/jawiki-country.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']
    
    return None

uk_text = read_wiki_data()

import re
# セクション名とレベルを抽出するパターン
# ==が多いほどレベルが深くなる（==はレベル1、===はレベル2、など）
pattern = r"^(={2,})\s*(.+?)\s*\1"

# 結果を格納するリスト
sections = []

# 各行に対してパターンマッチを行う
for line in uk_text.split('\n'):
    match = re.match(pattern, line)
    if match:
        level = len(match.group(1)) - 1  # ==の数からレベルを計算（==はレベル1）
        section_name = match.group(2)
        sections.append((section_name, level))

# 結果を表示
print("セクション名\tレベル")
for section_name, level in sections:
    print(f"{section_name}\t{level}")

