from gensim.models import KeyedVectors

# モデルの読み込み（バイナリ形式）
model_path = "GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 単語ベクトルの取得と表示
vector = model["United_States"]
print("United_Statesのベクトル（前10次元）:", vector[:10])  # 最初の10次元のみ表示
