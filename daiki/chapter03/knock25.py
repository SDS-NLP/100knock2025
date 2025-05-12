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
#re.MULTILINE：^ と $ が「行頭／行末」にマッチする
#re.DOTALL：. が改行にもマッチする
pattern = re.compile(r'^\{\{基礎情報.*?$(.*?)^}}$', 
re.MULTILINE | re.DOTALL)

m = pattern.search(uk_text)
infobox = m.group(1)

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

    info[key] = value 

print(info['首都'])
print(info['略名'])
