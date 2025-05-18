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

#[[ファイル:…]]のみを抜き出す
#(.*?)ここで得られた文字列が後で group(1) として取り出せる
pattern = re.compile(r'\[\[ファイル:(.*?)(?:\||\]\])')

#findall すると group(1) にあたる部分をリストで返す
files = pattern.findall(uk_text)

for file in files:
    print(file)