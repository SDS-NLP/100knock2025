# 国名に関する単語ベクトルに対し、Ward法による階層型クラスタリングを実行せよ。さらに、クラスタリング結果をデンドログラムとして可視化せよ。

from gensim.models import KeyedVectors
import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
import matplotlib_fontja

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

# Ward法による階層型クラスタリングを実行
country_vecs_array = np.array(country_vecs)

# Ward法による階層クラスタリング
linkage_matrix = linkage(country_vecs, method='ward')

# デンドログラムとして可視化
plt.figure(figsize=(15, 8))
dendrogram(linkage_matrix, labels=valid_countries)
plt.title('Ward法による国名の階層型クラスタリング')
plt.xlabel('国名')
plt.ylabel('距離')
plt.tight_layout()
plt.show()
