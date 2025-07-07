from gensim.models import KeyedVectors
import numpy as np
import torch

# 1. 学習済みの単語埋め込みをロード（バイナリ形式）
model_path = r"../../../GoogleNews-vectors-negative300.bin"
word_vectors = KeyedVectors.load_word2vec_format(model_path, binary=True, limit=100000)

# 2. PADトークン分 + 事前学習語彙数で行列を定義
vocab_size = len(word_vectors.key_to_index) + 1  # +1 は <PAD> のため
embedding_dim = word_vectors.vector_size         # 通常は 300

# 3. 埋め込み行列の初期化（先頭行をゼロベクトルに）
embedding_matrix = np.zeros((vocab_size, embedding_dim))

# 4. 単語とIDの辞書
token2id = {"<PAD>": 0}
id2token = {0: "<PAD>"}

# 5. 2行目以降に埋め込みを格納
max_vocab = 100000
for i, word in enumerate(word_vectors.index_to_key[:max_vocab], start=1):
    embedding_matrix[i] = word_vectors[word]
    token2id[word] = i
    id2token[i] = word

#embedding_matrix = torch.tensor(embedding_matrix, dtype=torch.float32)
embedding_matrix = torch.from_numpy(embedding_matrix).float()
