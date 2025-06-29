#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
from gensim.models import KeyedVectors
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

embedding_matrix, word2id, id2word = convert_w2v_to_embedding_matrix(w2v)
print("embedding_matrix 生成成功")

class BoWLogRegModel(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()

        self.emb = nn.Embedding.from_pretrained(embedding_matrix, freeze=True)

        self.linear = nn.Linear(embedding_matrix.shape[1], 1)

    def forward(self, input_ids):

        emb = self.emb(input_ids)        
        mean_emb = emb.mean(dim=1)       
        logits = self.linear(mean_emb)    
        probs = torch.sigmoid(logits)     
        return probs

model = BoWLogRegModel(embedding_matrix)

print(model)


# In[ ]:




