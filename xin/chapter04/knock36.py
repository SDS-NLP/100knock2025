import gzip
import json
import re
from collections import Counter
import MeCab
from tqdm import tqdm

tagger = MeCab.Tagger()

# 不要な記号を除去する正規表現関数
def clean_text(text):
    text = re.sub(r'\[\[.*?\|', '', text)  # [[記事名|表示名]] → 表示名
    text = re.sub(r'\[\[|\]\]', '', text)  # [[記事名]]
    text = re.sub(r'{{.*?}}', '', text)    # テンプレート
    text = re.sub(r'<.*?>', '', text)      # HTMLタグ
    text = re.sub(r'&[^;]+;', '', text)    # HTMLエンティティ
    text = re.sub(r"''+", '', text)        # 強調表現
    text = re.sub(r'=+', '', text)         # 見出し記号
    text = re.sub(r'\|+', '', text)        # テーブル・テンプレート
    text = re.sub(r'\*+', '', text)        # 箇条書き
    text = re.sub(r'-+', '', text)         # 罫線
    text = re.sub(r'/+', '', text)         # URLや区切り
    text = re.sub(r'\.+', '', text)        # ピリオド
    text = re.sub(r'[()\[\]{}]', '', text) # 括弧類
    return text

# 出現頻度カウント
word_counter = Counter()
valid_pos = {'名詞', '動詞', '形容詞', '副詞'}
exclude_surfaces = {'、', '。', '・', '|', '=', '-', '/', '.', '（', '）',':'}

with gzip.open('/home/tanxin/100knock2025/xin/chapter03/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in tqdm(f):
        article = json.loads(line)
        text = clean_text(article.get('text', ''))
        parsed = tagger.parse(text)
        for line in parsed.splitlines():
            if line == 'EOS' or line == '':
                continue
            parts = line.split('\t')
            if len(parts) < 2:
              continue
            surface = parts[0]
            features = parts[1].split(',')
            if surface in exclude_surfaces:
                 continue
            word_counter[surface] += 1
for word, count in word_counter.most_common(20):
    print(f'{word}: {count}')