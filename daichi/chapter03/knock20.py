import json
import gzip

# gzipファイルを開いて1行ずつ読み込む
with gzip.open('./daichi/chapter03/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in f:
        article = json.loads(line)  # JSON形式の文字列を辞書に変換
        if article['title'] == 'イギリス':
            uk_text = article['text']
            break

# 結果を表示
print(uk_text)
