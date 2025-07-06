import zipfile
import pandas as pd
import numpy as np
from scipy.stats import spearmanr

# zipファイルから読み込む
with zipfile.ZipFile('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter06/wordsim353.zip') as f:
    with f.open('combined.csv') as g:
        data = g.read()

# バイト列をデコード
data = data.decode('UTF-8').splitlines()
data = data[1:]

# タブ区切り
data = [line.split(',') for line in data]

# 単語ベクトルを読み込む
from gensim.models import KeyedVectors

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True
)
# 類似度を計算しdataに追加
for i, lst in enumerate(data):
    #sim = model.similarity(lst[0], lst[1])
    # ベクトルの内積を計算
    vector1 = model[lst[0]]
    vector2 = model[lst[1]]
    dot_product = np.dot(vector1, vector2)
    # ベクトルのノルムを計算
    norm1= np.linalg.norm(vector1)
    norm2 = np.linalg.norm(vector2)
    # コサイン類似度を計算
    cosine_similarity = dot_product / (norm1 * norm2)
    data[i].append(cosine_similarity)

# DataFrameに変換
df = pd.DataFrame(data, columns=['word1', 'word2', 'human', 'sim'])

# df[human]とdf[sim]のスピアマン相関係数を計算
correlation, p_value = spearmanr(df['human'], df['sim'])

print(f"スピアマン相関係数: {correlation}")




