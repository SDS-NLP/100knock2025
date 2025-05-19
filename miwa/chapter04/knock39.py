#39. Zipfの法則
import spacy
from collections import Counter
import matplotlib.pyplot as plt
import japanize_matplotlib
import numpy as np
japanize_matplotlib.japanize()

# 日本語モデルの読み込み（GiNZA）
nlp = spacy.load("ja_ginza")

# コーパスの読み込み
with open("kokoro.txt", "r", encoding="utf-8") as f:
    text = f.read()

# 分割サイズ（文字数）
chunk_size = 4000

words = []

# テキストをチャンクに分割して処理
for i in range(0, len(text), chunk_size):
    chunk = text[i:i+chunk_size]
    doc = nlp(chunk)
    words.extend([token.lemma_ for token in doc if token.is_alpha])

# 出現頻度計算
counter = Counter(words)
most_common = counter.most_common()

# 頻度順位と出現頻度のリスト作成
ranks = np.arange(1, len(most_common) + 1)
frequencies = np.array([freq for _, freq in most_common])


# log-logプロット
plt.figure(figsize=(8, 6))
plt.plot(ranks, frequencies)
plt.xscale('log')
plt.yscale('log')
plt.xlabel('出現頻度順位(log)')
plt.ylabel('出現頻度(log)')
plt.title('単語の出現頻度分布(Zipfの法則)')
plt.grid(True, which="both", ls="--", lw=0.5)
plt.tight_layout()
plt.savefig("zipf")
