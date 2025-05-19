from knock20 import uk_article_txt
import re
import collections

pattern = "(={2,4}.*?={2,4})"
result = re.findall(pattern, uk_article_txt)
section = {}

for text in result:
    # text
    c1 = collections.Counter(text)
    c2 = int(c1['=']/2) - 1
    text = text.replace('=', '')
    section[text] = c2

print(section)

"""
={2,4}: これは再び、2回以上4回以下の = に一致します。
( ... ): これはキャプチャグループを作成します。この部分に一致した文字列は後で参照することができます。
.: 任意の1文字に一致します。改行文字を除くすべての文字が対象です。
*: 直前の文字（この場合は.）が0回以上繰り返されることを意味します。つまり、任意の文字が0回以上続くことを許可します。
?: 直前の量指定子（この場合は*）を最短一致に変更します。通常、*はできるだけ多くの文字に一致しようとしますが、?を付けることで、最短の一致を探すようになります。
"""