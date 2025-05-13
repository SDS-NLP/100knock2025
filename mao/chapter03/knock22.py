"""
カテゴリ名の抽出
記事のカテゴリ名を(行単位ではなく名前で)抽出せよ
"""
from knock20 import uk_text
import re

pattern = "\[\[Category:(.*?)(?:\|.*?|)\]\]"
result = re.findall(pattern, uk_text)
print(result)
