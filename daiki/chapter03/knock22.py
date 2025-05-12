import gzip
import json
import re

path = 'daiki/chapter03/jawiki-country.json.gz'

uk_text = ""
with gzip.open(path, 'rt', encoding = 'utf-8') as file:
    for line in file:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            uk_text = article['text']
            break
category_lines = [line for line in uk_text.split('\n') if '[[Category:' in line]
for line in category_lines:
    match = re.search(r'\[\[Category:([^|\]]+)', line)
    #re.search(正規表現パターン, 対象文字列)
    #[ は特殊記号なので \[ と書く
    #[^|\]]+ は　| や ] 以外の文字を1文字以上
    #() で囲んでいるので、match.group(1) で取り出せる
    if match:
        print(match.group(1))
    #group(0) = [[Category:イギリス|*]]（全体）
    #group(1) = イギリスの政治
