#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
from torch.utils.data import Dataset
from gensim.models import KeyedVectors
import numpy as np

w2v_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"

print("Loading model...")
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

train_samples = [
    {'text': 'I love this movie', 'label': 1},
    {'text': 'This film was terrible', 'label': 0},
    {'text': 'Absolutely wonderful and inspiring', 'label': 1},
    {'text': 'I hate this so much', 'label': 0},
]
dev_samples = [
    {'text': 'What a great movie', 'label': 1},
    {'text': 'Awful and boring', 'label': 0},
]

def tokenize(text, word2id):
    return [word2id[word] for word in text.split() if word in word2id]

class SSTDataset(Dataset):
    def __init__(self, samples, word2id):
        self.data = []
        for sample in samples:
            input_ids = tokenize(sample['text'], word2id)
            if len(input_ids) == 0:
                continue 
            self.data.append({
                'text': sample['text'],
                'label': torch.tensor([float(sample['label'])]),
                'input_ids': torch.tensor(input_ids)
            })

    def __getitem__(self, idx): return self.data[idx]
    def __len__(self): return len(self.data)

train_dataset = SSTDataset(train_samples, word2id)
dev_dataset = SSTDataset(dev_samples, word2id)

sample = train_dataset[0]
print(sample)

