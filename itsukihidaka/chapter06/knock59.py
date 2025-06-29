# ベクトル空間上の国名に関する単語ベクトルをt-SNEで可視化せよ。

from gensim.models import KeyedVectors
import matplotlib.pyplot as plt
import matplotlib_fontja
import numpy as np
from sklearn.manifold import TSNE

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True
)

# 国名に関する単語リストを作成
with open('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter06/countries.txt', 'r') as f:
    countries = []
    for line in f:
        countries.append(line.strip())

# 国名に関する単語ベクトルを抽出（モデルに存在するもののみ）
country_vecs = []
valid_countries = []
for country in countries:
    if country in model:
        country_vecs.append(model[country])
        valid_countries.append(country)

# t-SNEで可視化
# ベクトルをnumpy配列に変換
country_vecs = np.array(country_vecs)

# t-SNEで次元削減（300次元→2次元）
tsne = TSNE(n_components=2, random_state=42)
country_2d = tsne.fit_transform(country_vecs)

# 可視化
plt.figure(figsize=(12, 8))
plt.scatter(country_2d[:, 0], country_2d[:, 1], alpha=0.7)

# 各点に国名をラベルとして表示
for i, country in enumerate(valid_countries):
    plt.annotate(country, (country_2d[i, 0], country_2d[i, 1]))

plt.title('t-SNEによる国名単語ベクトルの可視化')
plt.xlabel('t-SNE 第1成分')
plt.ylabel('t-SNE 第2成分')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

