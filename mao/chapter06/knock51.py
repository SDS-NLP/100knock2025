
"""knock51:単語の類似度
“United States”と”U.S.”のコサイン類似度を計算せよ。"""
from knock50 import vectors
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

vec_UnitedStates=vectors["United_States"]
vec_US=vectors["U.S."]

#コサイン類似度計算
if __name__=="__main__":
    similarity=cosine_similarity([vec_UnitedStates],[vec_US])[0][0]
    print(f"Cosine Similarity:{similarity:.4f}")