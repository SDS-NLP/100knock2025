# “United States”と”U.S.”のコサイン類似度を計算せよ。

from gensim.models import KeyedVectors
import numpy as np

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True)

print('メソッドを用いた結果:',model.similarity('United_States','U.S.'))

# 単語ベクトルを計算
vector_us = model['United_States']
vector_us_dot = model['U.S.']

# ベクトルの内積を計算
dot_product = np.dot(vector_us, vector_us_dot)

# ベクトルのノルムを計算
norm_us = np.linalg.norm(vector_us)
norm_us_dot = np.linalg.norm(vector_us_dot)

# コサイン類似度を計算
cosine_similarity = dot_product / (norm_us * norm_us_dot)

print('ベクトルの内積を計算した結果:',cosine_similarity)



