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

# 単語を抽出
words = []
for line in parsed.splitlines():
    if line == 'EOS' or line == '':
        continue
    word = line.split('\t')[0]
    words.append(word)

# 出現頻度をカウント
word_counts = Counter(words)

# 出現頻度の高い20語を取得
most_common_words = word_counts.most_common(20)

# 結果を表示
for word, count in most_common_words:
    print(f'{word}: {count}')