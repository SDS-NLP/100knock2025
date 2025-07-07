import numpy as np
from gensim.models import KeyedVectors

# モデルの読み込み（例: GoogleNews-vectors-negative300.bin）
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 語彙数と次元数
vocab = list(model.key_to_index.keys())
d_emb = model.vector_size
vocab_size = len(vocab) + 1  # +1 for <PAD>

# 埋め込み行列 E の初期化（1行目は<PAD>用に0ベクトル）
E = np.zeros((vocab_size, d_emb), dtype=np.float32)

# 単語 → ID / ID → 単語 の辞書作成
word2id = {"<PAD>": 0}
id2word = {0: "<PAD>"}

# ID 1から埋め込む
for i, word in enumerate(vocab, start=1):
    E[i] = model[word]
    word2id[word] = i
    id2word[i] = word

import numpy as np
import pickle

# 例: E = np.zeros((vocab_size, d_emb), dtype=np.float32)

np.save("embedding_matrix.npy", E)  # 拡張子は自動で .npy
with open("word2id.pkl", "wb") as f:
    pickle.dump(word2id, f)
