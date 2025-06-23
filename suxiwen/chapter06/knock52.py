import gensim.downloader as api
import numpy as np
from numpy.linalg import norm

# GloVeモデルのロード
model = api.load("glove-wiki-gigaword-100")

# ベクトルの平均で "United States" を表現
vec_us = (model['united'] + model['states']) / 2

# 上位10単語とその類似度を取得
similar_words = model.similar_by_vector(vec_us, topn=10)

# 出力
print("“United States” に類似した単語（上位10）:")
for word, score in similar_words:
    print(f"{word}: {score:.4f}")