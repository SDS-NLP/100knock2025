#あんまりわからない
import gzip
import json
import re 

path = 'daiki/chapter03/jawiki-country.json.gz'

uk_text = ""
with gzip.open(path, 'rt', encoding = 'utf-8') as file:
    for line in file:
        article = json.loads(line)
        if article['title'] == 'イギリス':
            uk_text = article['text']
            break

# 1. [[記事名#節名|表示文字]] → “表示文字”
uk_text = re.sub(
    r'\[\[[^|\]]+#[^|\]]*\|(.+?)\]\]',
    r'\1',
    uk_text
)

# 2. [[記事名|表示文字]] → “表示文字”
uk_text = re.sub(
    r'\[\[[^|\]]+\|(.+?)\]\]',
    r'\1',
    uk_text
)

# 3. [[記事名]] → “記事名”
uk_text = re.sub(
    r'\[\[([^|\]]+)\]\]',
    r'\1',
    uk_text
)

# 確認
print(uk_text)