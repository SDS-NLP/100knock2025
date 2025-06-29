#むずかしい
import gzip
import json
import re
import urllib.request
import urllib.parse

path = 'daiki/chapter03/jawiki-country.json.gz'

uk_text = ""
with gzip.open(path, 'rt', encoding = 'utf-8') as file:
    for line in file:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            uk_text = article['text']
            break
pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^}}$', 
re.MULTILINE | re.DOTALL)

m = pattern.search(uk_text)
infobox = m.group(1)
#辞書作成
info = {}
for line in infobox.split('\n'):
    line = line.strip()
    #行が空行 あるいは フィールド行でないのならcontinue で このループの残り処理を飛ばす
    if not line or not line.startswith('|'):
        continue
    #| フィールド名 = 値 という文字列から「フィールド名」と「値」を取り出す
    key, value = line[1:].split('=', 1)
    key = key.strip()
    value = value.strip()

#ここからurllibを使う
#もうわからない。あとで26-29復習する