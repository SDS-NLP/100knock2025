"""
テンプレートの抽出
記事中に含まれる「基本情報」テンプレートのフィールド名と値を抽出し、
辞書オブジェクトとして格納せよ
"""
import re
from knock20 import uk_text

pattern='基礎情報(.*?\<references/\>)'
result=re.findall(pattern, uk_text)
result[0] += "\\n"
pattern = '(?<=\\\\n\|)(.*?) *= *(.*?)(?=\\\\n)'
result2 = re.findall(pattern, result[0])
inf_dic = {}
for i, j in result2:
  inf_dic[i] = j
#print(inf_dic)
