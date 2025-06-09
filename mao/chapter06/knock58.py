"""
knock58 Ward法によるクラスタリング
国名に関する単語ベクトルに対し、Ward法による階層型クラスタリングを実行せよ。
さらに、クラスタリング結果をデンドログラムとして可視化せよ。
"""
from knock57 import countries
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from scipy.cluster.hierarchy import linkage, dendrogram
import numpy as np

# 1. 単語ベクトルの準備
# countries は ["Japan", "Germany", "France", ...] のようなリスト（前の knock57.py で作成したリストを利用）
# スペースを含む国名は "South_Korea" のようにアンダースコア化されている前提
from knock57 import countries  # または別モジュール名に合わせて調整

# モデルパス（環境に応じて変更）
model_path = 'mao/chapter06/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 2. ベクトルの抽出
vecs = []
valid_countries = []

for country in countries:
    if country in model:
        vecs.append(model[country])
        valid_countries.append(country)

vecs = np.array(vecs)

# 3. 階層クラスタリング（Ward法）
Z = linkage(vecs, method='ward')

# 4. デンドログラムの描画
plt.figure(figsize=(14, 7))
dendrogram(Z, labels=valid_countries, leaf_rotation=90)
plt.title("Hierarchical Clustering (Ward Method) of Country Vectors")
plt.xlabel("Country")
plt.ylabel("Distance")
plt.tight_layout()
plt.show()