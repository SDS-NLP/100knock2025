import json
import gzip

def uk_data():
    with gzip.open('/home/tanxin/100knock2025/xin/chapter03/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']  # ← dict ではなく本文だけを返す

# 関数を呼び出して、イギリスの記事本文を取得
uk_text = uk_data()
print(uk_text[:500])