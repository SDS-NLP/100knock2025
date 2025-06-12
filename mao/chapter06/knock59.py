"""
knock59:t-SNEによる可視化
ベクトル空間上の国名に関する単語ベクトルをt-SNEで可視化せよ。
"""
import numpy as np
from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# 国名リストの読み込み
with open("mao/chapter06/countries.txt", encoding="utf-8") as f:
    countries = [line.strip() for line in f if line.strip()]

# 学習済みWord2Vecモデルの読み込み（バイナリ形式）
model_path = "mao/chapter06/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 国名に対応するベクトルの取得（存在する単語だけに限定）
vecs = []
labels = []
for country in countries:
    if country in model:
        vecs.append(model[country])
        labels.append(country)

# t-SNEによる次元削減（2次元に圧縮）
tsne = TSNE(n_components=2, random_state=42, perplexity=30)

# t-SNE に渡す前に NumPy 配列に変換
vecs_np = np.array(vecs)

# t-SNE による次元圧縮
vecs_2d = tsne.fit_transform(vecs_np)

# 可視化
plt.figure(figsize=(14, 10))
plt.scatter(vecs_2d[:, 0], vecs_2d[:, 1])

# 各点にラベルを表示
for i, label in enumerate(labels):
    plt.annotate(label, (vecs_2d[i, 0], vecs_2d[i, 1]), fontsize=9)

plt.title("t-SNE visualization of country word vectors")
plt.grid(True)
plt.tight_layout()
plt.show()
