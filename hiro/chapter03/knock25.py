# 分からん

from knock20 import uk_article_txt
import re

pattern = '基礎情報(.*?\<references/\>)'
uk_bases = re.findall(pattern, uk_article_txt)
uk_bases[0] += "\\n"
pattern = '(?<=\\\\n\|)(.*?) *= *(.*?)(?=\\\\n)'
uk_bases_2 = re.findall(pattern, uk_bases[0])
inf_dic = {}
for i, j in uk_bases_2:
  inf_dic[i] = j
print(inf_dic)

"""
.: 任意の1文字に一致します。改行文字を除くすべての文字が対象です。
*: 直前の文字（この場合は.）が0回以上繰り返されることを意味します。つまり、任意の文字が0回以上続くことを許可します。
?: 直前の量指定子（この場合は*）を最短一致に変更します。通常、*はできるだけ多くの文字に一致しようとしますが、?を付けることで、最短の一致を探すようになります。
"""