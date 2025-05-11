# 26の処理に加えて、テンプレートの値からMediaWikiの内部リンクマークアップを除去し、テキストに変換せよ

import json

def read_wiki_data():
    file_path = '/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter03/jawiki-country.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']
    
    return None

uk_value = read_wiki_data()

import re

# 基礎情報テンプレートのフィールド名と値を抽出
pattern = r'^\{\{基礎情報.*?\n(.*?<references/>$)'
result = re.findall(pattern, uk_value, re.MULTILINE+re.VERBOSE+re.DOTALL)

templates = dict(re.findall(r'^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))', result[0], re.MULTILINE+re.VERBOSE+re.DOTALL))

# 強調マークアップを除去
for key, value in templates.items():
    # 弱い強調マークアップを除去
    pattern = r"('){2,5}"
    value = re.sub(pattern, '', value)

    pattern = r"(?<=\}\}\<br \/\>（)\[{2}"#<br />（フランス語]]:[[Dieu et mon droit|神と我が権利]]）
    value = re.sub(pattern, '', value)

    pattern = r"\[{2}.*?\|.*?px\|(?=.*?\]\])"#'[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]',
    value = re.sub(pattern, '', value)

    pattern = r"(?<=(\|))\[{2}"
    value = re.sub(pattern, '', value)

    pattern = r"(?<=\}{2}（)\[{2}"#スコットランド・ゲール語]]）\n*{{lang|cy
    value = re.sub(pattern, '', value)

    pattern = r"(?<=\>（)\[{2}.*?\|"#[[グレートブリテン及びアイルランド連合王国]]成立<br />（1800年合同法]]）
    value = re.sub(pattern, '', value)

    pattern = r"(?<=（.{4}).*?\[{2}.*?\)\|" #'[[イングランド王国]]／[[スコットランド王国]]<br />（両国とも[[合同法 (1707年)|1707年合同法]]まで）',
    value = re.sub(pattern, '', value)

    pattern = r"\[{2}.*?\|"#[[(除去)|]]の処理
    value = re.sub(pattern, '', value)

    pattern = r"(\[{2}|\]{2})"#最後に残ったやつを処理
    templates[key] = re.sub(pattern, '', value)

from pprint import pprint
pprint(templates)