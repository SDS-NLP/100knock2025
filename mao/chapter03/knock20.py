"""
Wikipedia記事のJSONファイルを読み込み、「イギリス」に関する記事本文を表示せよ。
問題21-29では、、ここで抽出した記事本文に対して実行せよ。
"""

import json
import re

text_list = []
file_path = 'mao/chapter03/jawiki-country.json'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        text_list.append(json.loads(line))
for i in range(len(text_list)):
    if text_list[i]['title']=="イギリス":
        uk_text = str(text_list[i])
        break

#print(uk_text)
#このままにしておくと他のファイルでもuk_textが出力されてしまう