# 25の処理時に、テンプレートの値からMediaWikiの強調マークアップ（弱い強調、強調、強い強調のすべて）を除去してテキストに変換せよ

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

# 基礎情報テンプレートのフィールド名と値を抽出
pattern = r'^\{\{基礎情報.*?\n(.*?<references/>$)'
result = re.findall(pattern, uk_text, re.MULTILINE+re.VERBOSE+re.DOTALL)

templates = dict(re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', result[0], re.MULTILINE+re.VERBOSE+re.DOTALL))

# 強調マークアップを除去
for key, value in templates.items():
    # 弱い強調マークアップを除去
    templates[key] = re.sub(r"('){2,5}" , '', value)
    
from pprint import pprint
pprint(templates)