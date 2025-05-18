import re
import json
import gzip
from knock20 import uk_data
from knock21 import extract_categories

uk_text = uk_data()
category_lines = extract_categories(uk_text)

def extract_category_names(category_lines):
    pattern = r'^\[\[Category:(.*?)\]\]$'
    for cat in category_lines:
        match = re.match(pattern, cat)
        if match:
            category_name = match.group(1).split('|')[0]
            yield category_name

# ジェネレータをリストに変換して表示
category_names = list(extract_category_names(category_lines))
for name in category_names:
    print(name)
