import gzip #.gz形式のファイルを扱うライブラリ
import json #json文字列とpythonデータ構造を相互変換

path = 'daiki/chapter03/jawiki-country.json.gz'

with gzip.open(path, 'rt', encoding = 'utf-8') as file:
    for line in file:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            print(article['text'])
            break