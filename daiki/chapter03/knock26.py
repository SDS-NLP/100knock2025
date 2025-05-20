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

# 1. 強調マークアップ (''  '', '''  ''', '''''  ''''') の除去
uk_text = re.sub(r"'{2,5}", '', uk_text)

# 2. 内部リンク
#  2-1. [[記事名|表示文字]] → “表示文字”
uk_text = re.sub(r'\[\[[^|\]]+\|([^|\]]+)\]\]', r'\1', uk_text)
#  2-2. [[記事名#節名|表示文字]] → “表示文字”
uk_text = re.sub(r'\[\[[^|\]]+#.+?\|([^|\]]+)\]\]', r'\1', uk_text)
#  2-3. [[記事名]] → “記事名”
uk_text = re.sub(r'\[\[([^#|\]]+?)(?:#[^|\]]*?)?\]\]', r'\1', uk_text)

# 3. ファイル参照
#  [[File:xxx.png|…|説明文]] や [[ファイル:xxx.png|説明文]] → “説明文”
uk_text = re.sub(
    r'\[\[(?:File|ファイル):[^|\]]*'
    r'(?:\|.*?\|)?'                  # サムネイルオプションなどを飛ばして
    r'([^|\]]*?)'                    # キャプション (≈ 説明文)
    r'\]\]',
    r'\1',
    uk_text
    )

# 4. 外部リンク
#  4-1. [https://… 表示文字] → “表示文字”
uk_text = re.sub(r'\[https?://[^\s\]]+\s+([^\]]+)\]', r'\1', uk_text)
#  4-2. [https://…] → “https://…”
uk_text = re.sub(r'\[(https?://[^\]]+)\]', r'\1', uk_text)

# 5. カテゴリ
#  [[Category:…]] はまるごと削除
uk_text = re.sub(r'\[\[Category:[^\]]+\]\]', '', uk_text)

# 6. リダイレクト
#  #REDIRECT [[記事名]] 形式の行をまるごと削除
uk_text = re.sub(r'(?mi)^#REDIRECT\s+\[\[.+?\]\]\s*$', '', uk_text)

print(uk_text)
