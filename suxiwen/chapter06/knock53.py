import gensim.downloader as api

# モデル読み込み（100次元 GloVe）
model = api.load("glove-wiki-gigaword-100")

# ベクトル演算: Spain - Madrid + Athens
result_vector = model['spain'] - model['madrid'] + model['athens']

# 類似語の取得（上位10語）
similar_words = model.similar_by_vector(result_vector, topn=10)

# 結果表示
print("Spain - Madrid + Athens に類似した単語（上位10）:")
for word, similarity in similar_words:
    print(f"{word}: {similarity:.4f}")