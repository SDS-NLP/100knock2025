import torch
from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score
from knock72 import train_data, embedding_matrix, BoWLogisticRegression, compute_avg_embedding, SSTDataset
import numpy as np
import torch.nn as nn

# collate_fn の定義（バッチ整形）
def collate_fn(batch):
    input_ids = [item["input_ids"] for item in batch]
    labels = torch.stack([item["label"] for item in batch])
    return {"input_ids": input_ids, "label": labels}

# DataLoaderの準備
train_dataset = SSTDataset(train_data)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)

# モデルと損失関数・最適化
embedding_tensor = torch.tensor(embedding_matrix)  # numpy → tensor
model = BoWLogisticRegression(embedding_dim=embedding_tensor.shape[1])
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# 学習ループ（例：10エポック）
num_epochs = 10
model.train()
for epoch in range(num_epochs):
    total_loss = 0
    for batch in train_loader:
        input_ids = batch["input_ids"]
        labels = batch["label"].squeeze(1)

        # 平均ベクトルを取得（埋め込み行列は学習しない＝固定）
        avg_emb = compute_avg_embedding(input_ids, embedding_tensor)

        # 順伝播 → 損失計算 → 学習
        logits = model(avg_emb)
        loss = criterion(logits, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"[Epoch {epoch+1}] Loss: {avg_loss:.4f}")
