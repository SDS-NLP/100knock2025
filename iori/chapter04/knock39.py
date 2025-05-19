import MeCab
import ipadic
from collections import Counter
import re
import matplotlib.pyplot as plt

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

# 単語の出現頻度をカウント
word_counts = Counter(words)

# 順位と頻度を取得
frequencies = sorted(word_counts.values(), reverse=True)
ranks = range(1, len(frequencies) + 1)

# 両対数グラフをプロット
plt.figure(figsize=(10, 6))
plt.loglog(ranks, frequencies, marker="o", linestyle="none")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.title("Zipf's Law: Rank vs Frequency")
plt.grid(True, which="both", linestyle="--", linewidth=0.5)
plt.show()