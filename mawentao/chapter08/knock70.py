#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gensim.models import KeyedVectors
import torch
import numpy as np

w2v_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"

print("Loading Word2Vec model...")
w2v = KeyedVectors.load_word2vec_format(w2v_path, binary=True)
print("Loaded!")

def convert_w2v_to_embedding_matrix(w2v_model, max_vocab=50000):
    word2id = {'<PAD>': 0}
    vectors = [np.zeros(w2v_model.vector_size)]

    for i, word in enumerate(w2v_model.index_to_key[:max_vocab]):
        word2id[word] = len(vectors)
        vectors.append(w2v_model[word])

    embedding_matrix = torch.tensor(np.array(vectors), dtype=torch.float32)
    id2word = {v: k for k, v in word2id.items()}

    return embedding_matrix, word2id, id2word

embedding_matrix, word2id, id2word = convert_w2v_to_embedding_matrix(w2v, max_vocab=50000)

print(f"語彙数（PAD含む）: {len(word2id)}") 
print(f"埋め込み行列のサイズ: {embedding_matrix.shape}") 
print(f"<PAD>のベクトル（前5次元）: {embedding_matrix[0][:5]}")
print(f"'king'のID: {word2id.get('king', '未登録')}")
print(f"IDから単語へ: {id2word.get(123)}")

