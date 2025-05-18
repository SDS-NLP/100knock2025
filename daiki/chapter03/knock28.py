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
text = uk_text

# 1. 強調マークアップ (''、'''、''''') の除去
text = re.sub(r"'{2,5}", '', text)

# 2. 内部リンクの除去（27 の処理）
# 2-1. [[記事名#節|表示]] → “表示”
text = re.sub(r'\[\[[^|\]]+#[^|\]]*\|(.+?)\]\]', r'\1', text)
# 2-2. [[記事名|表示]] → “表示”
text = re.sub(r'\[\[[^|\]]+\|(.+?)\]\]', r'\1', text)
# 2-3. [[記事名]] → “記事名”
text = re.sub(r'\[\[([^|\]]+)\]\]', r'\1', text)

# 3. ファイル参照の除去（25 の処理を応用）
# [[File:xxx|…|キャプション]] や [[ファイル:xxx|キャプション]] → “キャプション”
text = re.sub(
    r'\[\[(?:File|ファイル):[^\]]*?\|(?:.*?\|)?([^\|\]]*?)\]\]',
    r'\1',
    text
)

# 4. 外部リンクの除去
# 4-1. [http://… 表示] → “表示”
text = re.sub(r'\[https?://[^\s\]]+\s+([^\]]+)\]', r'\1', text)
# 4-2. [http://…] → “http://…”
text = re.sub(r'\[(https?://[^\]]+)\]', r'\1', text)

# 5. HTML コメントの除去
text = re.sub(r'<!--.*?-->', '', text, flags=re.S)

# 6. <ref> タグの除去
text = re.sub(r'<ref[^>]*>.*?</ref>', '', text, flags=re.S)
text = re.sub(r'<ref[^/]*/>', '', text)

# 7. その他の HTML タグの除去
text = re.sub(r'<[^>]+>', '', text)

# 8. テンプレート ({{…}}) の除去
# ネストを考えて「最内側」から順に消す
tpl_pat = re.compile(r'\{\{[^{}]*\}\}')
while tpl_pat.search(text):
    text = tpl_pat.sub('', text)

# 9. HTMLエンティティの除去（例: &nbsp; &amp; など）
text = re.sub(r'&(?:nbsp|amp|quot|lt|gt);', '', text)

print(text)