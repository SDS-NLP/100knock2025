import MeCab
import ipadic
from collections import Counter
import re

# ファイルを読み込む
with open('kokoro.txt', 'r', encoding='utf-8') as f:
    text = f.read()

    # 《》で囲まれた部分を削除
    text = re.sub(r'《.*?》', '', text)

# MeCabで形態素解析
mecab = MeCab.Tagger(ipadic.MECAB_ARGS)
parsed = mecab.parse(text)

# 名詞を抽出
nouns = []
for line in parsed.splitlines():
    if line == 'EOS' or line == '':
        continue
    parts = line.split('\t')
    if len(parts) > 1:
        features = parts[1].split(',')
        if features[0] == '名詞':
            nouns.append(parts[0])

# 出現頻度をカウント
noun_counts = Counter(nouns)

# 出現頻度の高い20語を表示
for word, count in noun_counts.most_common(20):
    print(f'{word}: {count}')