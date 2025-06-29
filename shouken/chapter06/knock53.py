from gensim.models import KeyedVectors

# モデルの読み込み（GoogleNews vectors）
model_path = "GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# アナロジーベクトルの計算：Spain - Madrid + Athens
result = model.most_similar(positive=["Athens", "Spain"], negative=["Madrid"], topn=10)

# 結果の表示
for word, score in result:
    print(f"{word}: {score:.4f}")
