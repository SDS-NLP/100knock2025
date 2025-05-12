"""
記事中でカテゴリ名を宣言している行を抽出せよ。
"""
from knock20 import uk_text
import re

#カテゴリー名を行を抽出する
#\[\[  \]\]:特殊文字をエスケープして文字として指定
#Category::そのまま
#.*:任意の文字列が0回以上繰り返される
pattern="\[\[Category:.*\]\]"
result=re.findall(pattern, uk_text)
print(result)

