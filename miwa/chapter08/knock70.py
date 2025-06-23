#70. 単語埋め込みの読み込み
from gensim.models import KeyedVectors
import numpy as np

def load_word2vec_bin(embedding_path, max_vocab_size=None):
    print("Word2Vecモデルを読み込み")
    model = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
    print("モデル読み込み完了")

    d_emb = model.vector_size  # 埋め込みの次元（GoogleNewsは300）
    word2id = {'<PAD>': 0}
    id2word = {0: '<PAD>'}
    embedding_vectors = [np.zeros(d_emb, dtype=np.float32)]  # E[0] ← ゼロベクトル

    # 語彙を順番に追加（必要なら max_vocab_size で制限）
    for i, word in enumerate(model.index_to_key):
        if max_vocab_size and len(word2id) >= max_vocab_size:
            break
        vector = model[word]
        idx = len(word2id)
        word2id[word] = idx
        id2word[idx] = word
        embedding_vectors.append(vector)

    E = np.vstack(embedding_vectors)

    print(f"語彙数（<PAD>含む）: {E.shape[0]}")
    print(f"埋め込み次元: {E.shape[1]}")
    return E, word2id, id2word

embedding_path = "chapter06/GoogleNews-vectors-negative300.bin.gz"
E, word2id, id2word = load_word2vec_bin(embedding_path, max_vocab_size=50000)
