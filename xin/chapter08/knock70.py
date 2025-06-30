import numpy as np
import gensim.downloader as api

# ここではglove-wiki-gigaword-100（約40万語、100次元）を使用
print("Loading embedding...")
model = api.load("glove-wiki-gigaword-100")  # 100次元
print("Embedding loaded.")

# 語彙数と次元数
vocab_size = len(model.key_to_index) + 1  # +1 for <PAD>
embedding_dim = model.vector_size

# 埋め込み行列（先頭行はゼロベクトルで<PAD>用）
embedding_matrix = np.zeros((vocab_size, embedding_dim), dtype=np.float32)

# 単語⇔インデックス辞書の初期化
word2idx = {"<PAD>": 0}
idx2word = {0: "<PAD>"}

# 埋め込み行列を構築
for idx, word in enumerate(model.key_to_index, start=1):
    embedding_matrix[idx] = model[word]
    word2idx[word] = idx
    idx2word[idx] = word

print(f"Embedding matrix shape: {embedding_matrix.shape}")