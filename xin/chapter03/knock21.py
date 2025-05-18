import re
import gzip
from knock20 import uk_data

# イギリス記事の本文を取得
uk_text = uk_data()

# カテゴリ行の抽出
def extract_categories(text):
    # 正規表現パターンを定義
    pattern = r'^\[\[Category:.*?\]\]'
    # カテゴリ行を抽出
    category_lines = re.findall(pattern, text, re.MULTILINE)
    return category_lines

category_lines = extract_categories(uk_text)

# 結果を表示
for line in category_lines:
    print(line)