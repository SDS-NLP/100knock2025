from gensim.models import KeyedVectors

# モデルのパス
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'

# モデルの読み込み
model = KeyedVectors.load_word2vec_format(model_path, binary=True)


word = 'United_States'

# ベクトルの取得と表示
vector = model[word]
print(f"{word} のベクトル（次元数 {len(vector)}）:\n")
print(vector)

