# 記事から参照されているメディアファイルをすべて抜き出せ。

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

pattern = r"\[\[ファイル:(.*?)(?:\|.*?|)\]\]"
result = re.findall(pattern, uk_text)
print(result)