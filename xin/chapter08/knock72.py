import torch
import torch.nn as nn
from knock71 import train_data, embedding_model, word2idx
import numpy as np

# GloVe埋め込みベクトルを行列に変換
embedding_dim = embedding_model.vector_size
vocab_size = len(word2idx)
embedding_matrix = np.zeros((vocab_size, embedding_dim), dtype=np.float32)

for word, idx in word2idx.items():
    if word == "<PAD>":
        continue
    embedding_matrix[idx] = embedding_model[word]

class BoWLogisticRegression(nn.Module):
    def __init__(self, embedding_dim):
        super(BoWLogisticRegression, self).__init__()
        self.linear = nn.Linear(embedding_dim, 1)  # 単層

    def forward(self, x):
        return self.linear(x).squeeze(1)  # shape: (batch,)
# BoWモデルの平均ベクトルを計算する関数
def compute_avg_embedding(input_ids, embedding_matrix):

        batch_embeddings = []
        for ids in input_ids:
            vecs = [embedding_matrix[i] for i in ids if i != 0]  # <PAD>除外
            if len(vecs) == 0:
                avg = torch.zeros(embedding_matrix.shape[1])
            else:
                avg = torch.stack(vecs).mean(dim=0)
            batch_embeddings.append(avg)
        return torch.stack(batch_embeddings)

from torch.utils.data import DataLoader

# DataLoader 用にカスタム Dataset
class SSTDataset(torch.utils.data.Dataset):
    def __init__(self, examples):
        self.examples = examples

    def __len__(self):
        return len(self.examples)

    def __getitem__(self, idx):
        return self.examples[idx]

train_dataset = SSTDataset(train_data)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

# モデルと損失・最適化
embedding_tensor = torch.tensor(embedding_matrix)  # numpy → tensor
model = BoWLogisticRegression(embedding_dim=embedding_tensor.shape[1])
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)
model.train()
def collate_fn(batch):
    input_ids = [item["input_ids"] for item in batch]
    labels = torch.stack([item["label"] for item in batch])
    return {"input_ids": input_ids, "label": labels}
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)
for batch in train_loader:
    input_ids = batch["input_ids"]
    labels = batch["label"]

    avg_emb = compute_avg_embedding(input_ids, embedding_tensor)
    logits = model(avg_emb)
    loss = criterion(logits, labels.squeeze(1))

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

print(f"Loss: {loss.item():.4f}")
