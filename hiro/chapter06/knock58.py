import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from gensim.models import KeyedVectors # Word2Vecモデル
from scipy.cluster.hierarchy import dendrogram, linkage

# データの読み込みと前処理
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, "questions-words.txt")
df = pd.read_csv(csv_path, sep=" ")
df = df.reset_index()
df.columns = ["v1", "v2", "v3", "v4"]
df.dropna(inplace=True)
df = df.iloc[:5030]
country = list(set(df["v4"].values))

# Word2Vecモデルの読み込み
model_path = os.path.join(script_dir, 'GoogleNews-vectors-negative300.bin')
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 国名と国名ベクトルの変数格納
countryName = []
countryVec = []
for c in country:
    countryName.append(c)
    countryVec.append(model[c])

# 階層型クラスタリング
X = np.array(countryVec)
linkage_result = linkage(X, method="ward", metric="euclidean")

# デンドログラムの可視化
plt.figure(num=None, figsize=(16, 9), dpi=200, facecolor="w", edgecolor="k")
dendrogram(linkage_result, labels=countryName)
plt.show()