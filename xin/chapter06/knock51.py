import gensim.downloader as api
import numpy as np
from numpy.linalg import norm

# モデルロード
model = api.load("glove-wiki-gigaword-100")

# ベクトル平均で united_states を構成
vec_us = (model['united'] + model['states']) / 2
vec_u_s = model['u.s.']

# コサイン類似度関数
def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))
#- 内積 np.dot(a, b) を、それぞれのベクトルのノルムの積 (norm(a) * norm(b)) で割る。
#- ベクトルのノルムは numpy.linalg.norm を使用して計算する。
# 類似度表示
similarity = cosine_similarity(vec_us, vec_u_s)
print(f"united_states と u.s. のコサイン類似度: {similarity:.4f}")
