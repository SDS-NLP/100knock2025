import gzip
import json
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
from janome.tokenizer import Tokenizer
from knock36 import clean_text
file_path = "/home/tanxin/100knock2025/xin/chapter03/jawiki-country.json.gz"
output_png="freq_loglog.png"

plt.rcParams['font.family']= ['Noto Sans CJK JP']
plt.rcParams['axes.unicode_minus'] = False
# 形態素解析器の初期化
tokenizer = Tokenizer()
word_counts = Counter()

# Wikipediaコーパスの単語頻度を計算
with gzip.open(file_path, "rt", encoding="utf-8") as f:
    for line in f:
        article = json.loads(line)
        text = clean_text(article.get('text', ''))
        tokens = tokenizer.tokenize(text)

        # 名詞を対象に単語の頻度をカウント
        for token in tokens:
            if "名詞" in token.part_of_speech:
                word_counts[token.surface] += 1

# 出現頻度順にソート
sorted_counts = sorted(word_counts.values(), reverse=True)

# 順位（1位, 2位, ...）
ranks = np.arange(1, len(sorted_counts) + 1)

# 両対数グラフのプロット
plt.figure(figsize=(8, 6))
plt.loglog(ranks, sorted_counts, marker="o", linestyle="None", markersize=4)

plt.xlabel("Rank (単語の頻度順位)")
plt.ylabel("Frequency (出現頻度)")
plt.title("単語の出現頻度分布 (Zipfの法則)")
plt.grid(True, which="both", linestyle="--")

plt.tight_layout()
plt.savefig(output_png, dpi=300, bbox_inches="tight")
print(f">>> 両対数プロットを '{output_png}' に保存しました。")