#!/usr/bin/env python
# coding: utf-8

# In[3]:


import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from gensim.models import KeyedVectors
import numpy as np

# === 1. 加载 Word2Vec 模型 ===
w2v_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin" 
print("Loading Word2Vec model...")
w2v = KeyedVectors.load_word2vec_format(w2v_path, binary=True)
print("Loaded!")

# === 2. 转换为 embedding_matrix ===
def convert_w2v_to_embedding_matrix(w2v_model, max_vocab=50000):
    word2id = {'<PAD>': 0}
    vectors = [np.zeros(w2v_model.vector_size)]
    for word in w2v_model.index_to_key[:max_vocab]:
        word2id[word] = len(vectors)
        vectors.append(w2v_model[word])
    embedding_matrix = torch.tensor(np.array(vectors), dtype=torch.float32)
    id2word = {v: k for k, v in word2id.items()}
    return embedding_matrix, word2id, id2word

embedding_matrix, word2id, id2word = convert_w2v_to_embedding_matrix(w2v)
print("embedding_matrix 生成成功")

# === 3. 模型定义（BoW + Logistic Regression） ===
class BoWLogRegModel(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        self.emb = nn.Embedding.from_pretrained(embedding_matrix, freeze=True)  # 冻结
        self.linear = nn.Linear(embedding_matrix.shape[1], 1)

    def forward(self, input_ids):
        emb = self.emb(input_ids)              # (batch_size, seq_len, 300)
        mean_emb = emb.mean(dim=1)             # (batch_size, 300)
        logits = self.linear(mean_emb)         # (batch_size, 1)
        probs = torch.sigmoid(logits)          # (batch_size, 1)
        return probs

# === 4. 构造简单的训练样本（词ID + 标签）===
# 示例数据（用实际数据时请替换）
# 假设 “hello world” 和 “goodbye world” 分别是正例与负例
sample_sentences = [
    ["hello", "world"],
    ["goodbye", "world"]
]
sample_labels = [1, 0]  # 正类、负类

# 句子 → ID序列（最多填充到4个词）
max_len = 4
X_ids = []
for sent in sample_sentences:
    ids = [word2id.get(w, 0) for w in sent]
    ids += [0] * (max_len - len(ids))
    X_ids.append(ids)
X_tensor = torch.tensor(X_ids, dtype=torch.long)
y_tensor = torch.tensor(sample_labels, dtype=torch.float32).unsqueeze(1)

# 数据集和 DataLoader
dataset = TensorDataset(X_tensor, y_tensor)
loader = DataLoader(dataset, batch_size=2, shuffle=True)

# === 5. 模型训练设置 ===
model = BoWLogRegModel(embedding_matrix)
criterion = nn.BCELoss()
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001)

# === 6. 训练循环 ===
EPOCHS = 10
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0.0
    for batch_x, batch_y in loader:
        optimizer.zero_grad()
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss:.4f}")

