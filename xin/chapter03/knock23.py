import json
import gzip
import re
from knock20 import uk_data
#記事中に含まれるセクション名とそのレベル（例えば”== セクション名 ==”なら1）を表示せよ。
uk_text = uk_data()
pattern=r"^(={2,})\s*(.*?)\s*\1$"
#  ^(={2,}) → 行の先頭にある2つ以上の =（例: ==, ===）を取得。
#  \s*(.*?)\s* → = に囲まれた見出しのタイトル部分を取得（前後の空白は省略）。
#  \1$ → 行の末尾にも同じ数の = があることを確認。

sections = re.findall(pattern, uk_text, re.MULTILINE)
# re.findall は、Python の正規表現モジュール re で、指定された文字列の中で正規表現パターンに一致するすべての文字列をリストとして返す関数
# この過程によってsecotions には、見出しのレベルとタイトルがタプルとして格納される。
# eg. sections = [("==", "歴史"),("===", "近代"),("====", "第二次世界大戦後")]

for level, title in sections:
    print(f"Level: {len(level) - 1}, Title: {title}")