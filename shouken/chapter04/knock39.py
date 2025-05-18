import matplotlib.pyplot as plt
from fugashi import GenericTagger
from collections import Counter

tagger = GenericTagger("-r /etc/mecabrc -d /var/lib/mecab/dic/debian")

with open("kokoro.txt", encoding="utf-8") as f:
    text = f.read()

# 形態素解析して単語表層を抽出
words = [word.surface for word in tagger(text)]

# 単語頻度をカウント
counter = Counter(words)

# 頻度の高い順に並べて順位と頻度を取得
freqs = sorted(counter.values(), reverse=True)
ranks = range(1, len(freqs) + 1)

# 両対数グラフで描画
plt.figure(figsize=(8,6))
plt.loglog(ranks, freqs)
plt.title("Zipf's Law (kokoro.txt)")
plt.xlabel("Rank")
plt.ylabel("Frequency")
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.savefig("zipf.png")
