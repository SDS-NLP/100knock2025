import gzip
import json
import re

path = 'daiki/chapter03/jawiki-country.json.gz'
#uk_textの作成
uk_text = ""
with gzip.open(path, 'rt', encoding = 'utf-8') as file:
    for line in file:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            uk_text = article['text']
            break

pattern = re.compile(r'^(=+)\s*(.*?)\s*\1$')
#セクション見出しをキャプチャするための正規表現

for line in uk_text.split('\n'):
    m = pattern.match(line)
    #line の先頭から、pattern（セクション見出しの形式）に完全一致するかを調べる
    if m:
        #m.group(1)は'=='などの等号の列
        equal = m.group(1)
        #等号の数−１がレベル
        level = len(equal) - 1
        #m.group(2)が見出しの中身
        title = m.group(2)
        print(f'レベル{level}：{title}')