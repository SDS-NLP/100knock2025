# テンプレートの内容を利用し、国旗画像のURLを取得せよ。（ヒント: MediaWiki APIのimageinfoを呼び出して、ファイル参照をURLに変換すればよい）

# 27の処理に加えて、テンプレートの値からMediaWikiマークアップを可能な限り除去し、国の基本情報を整形せよ。

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
    value = re.sub(pattern, '', value)

    pattern = r'\{\{.*?\{\{center\|' #{{center|ファイル:United States Navy Band - God Save the Queen.ogg}}',
    value = re.sub(pattern, '', value)

    pattern = r'\{\{.*?\|.*?\|.{2}\|'
    value = re.sub(pattern, '', value) #'{{仮リンク|リンゼイ・ホイル|en|Lindsay Hoyle}}'

    pattern = r'\<ref.*?\>.*?\<\/ref\>'#<ref>で囲んでいるもの
    value = re.sub(pattern, '', value)

    pattern = r'\<ref.*?\>|\<br \/\>'#<ref>単体+<br />単体
    value = re.sub(pattern, '', value)

    pattern = r'\{\{lang\|.*?\|'#公式国名、標語の外国語タイトルを消すため
    value = re.sub(pattern, '', value)

    pattern = r'\{\{.*?\}\}'#確立年月日2,3,4の{を除去する
    value = re.sub(pattern, '', value)

    pattern = r'\}\}'# 公式国名、標語、国家、他元首等氏名2の}を除去する   
    templates[key] = re.sub(pattern, '', value)

import requests

def get_flag_image_url(templates):
    # 国旗画像のファイル名を取得
    flag_filename = templates['国旗画像']
    url = f'https://en.wikipedia.org/w/api.php?action=query&titles=File:{flag_filename}&prop=imageinfo&iiprop=url&format=json'
    response = requests.get(url)
    data = response.json()  

    # ファイル参照をURLに変換
    file_url = data['query']['pages']['23473560']['imageinfo'][0]['url']
    return file_url

print(get_flag_image_url(templates))