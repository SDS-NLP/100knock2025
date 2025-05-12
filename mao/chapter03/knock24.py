"""
ファイル参照の抽出
記事から参照されているメディアファイルをすめて抜き出せ
"""
import re
from knock20 import uk_text

#[[ファイル:...]]にマッチ
pattern='\[\[ファイル:(.*?)(?:\||\])'
result=re.findall(pattern, uk_text)

#実行結果
print(result)
