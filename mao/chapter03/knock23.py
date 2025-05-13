"""
セクション構造
記事中に含まれるセクション名とそのレベル名を表示せよ
"""
from knock20 import uk_text
import collections
import re

pattern="(={2,4}.*?={2,4})"
result=re.findall(pattern, uk_text)
section={}
for text in result:
    c1=collections.Counter(text)
    c2=int(c1['=']/2) - 1
    text=text.replace('=', '')
    section[text]=c2

print(section)
