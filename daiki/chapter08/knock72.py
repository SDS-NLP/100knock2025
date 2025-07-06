import torch
import torch.nn as nn
import numpy as np
import pickle
from knock71 import train_data, dev_data

# 単語埋め込み行列の読み込み
E = np.load("embedding_matrix.npy")
embedding_matrix = torch.from_numpy(E).float()  # torch.Tensor へ変換

# word2id も使いたければ
with open("word2id.pkl", "rb") as f:
    word2id = pickle.load(f)

# 埋め込み行列 E を torch.Tensor に変換
embedding_matrix = torch.tensor(E, dtype=torch.float32)

# 埋め込みレイヤー
embedding = nn.Embedding.from_pretrained(embedding_matrix, freeze=True)  # freeze=True: 埋め込みを更新しない

# ロジスティック回帰モデル
class BoWClassifier(nn.Module):
    def __init__(self, embedding):
        super().__init__()
        self.embedding = embedding
        self.linear = nn.Linear(embedding.embedding_dim, 1)

    def forward(self, input_ids):
        embedded = self.embedding(input_ids)                # [batch_size, seq_len, dim]
        averaged = embedded.mean(dim=1)                     # [batch_size, dim]
        output = self.linear(averaged).squeeze(1)           # [batch_size]
        return output

model = BoWClassifier(embedding)
criterion = nn.BCEWithLogitsLoss()  # ロジットを直接扱うので Sigmoid 不要
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

def collate_batch(batch):
    input_ids = [ex["input_ids"] for ex in batch]
    labels = [ex["label"] for ex in batch]
    input_ids = nn.utils.rnn.pad_sequence(input_ids, batch_first=True, padding_value=0)
    labels = torch.cat(labels)
    return input_ids, labels

# train_data をミニバッチにして使う
from torch.utils.data import DataLoader

train_loader = DataLoader(train_data, batch_size=32, shuffle=True, collate_fn=collate_batch)

for epoch in range(5):
    for input_ids, labels in train_loader:
        optimizer.zero_grad()
        logits = model(input_ids)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

model.eval()
with torch.no_grad():
    input_ids, labels = collate_batch(dev_data)
    logits = model(input_ids)
    predictions = (torch.sigmoid(logits) >= 0.5).float()
    accuracy = (predictions == labels).float().mean()
    print(f"Accuracy: {accuracy.item():.4f}")

#出力
"""
train: 66650
dev: 872
{'text': 'hide new secretions from the parental units ', 'label': tensor([0.]), 'input_ids': tensor([  5785,     66, 113845,     18,     12,  15095,   1594])}
Accuracy: 0.7752
"""