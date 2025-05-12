from knock20 import uk_article_txt
import re

pattern = "\[\[Category:.*?\]\]"
uk_category_lines = re.findall(pattern, uk_article_txt)
print(uk_category_lines)

"""
.: 任意の1文字に一致します。改行文字を除くすべての文字が対象です。
*: 直前の文字（この場合は.）が0回以上繰り返されることを意味します。つまり、任意の文字が0回以上続くことを許可します。
?: 直前の量指定子（この場合は*）を最短一致に変更します。通常、*はできるだけ多くの文字に一致しようとしますが、?を付けることで、最短の一致を探すようになります。
"""