# 遅すぎて動かない gpuが必要
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import pickle
from tqdm import tqdm
from knock73 import BoWClassifier, embedding, collate_batch, load_sst_data, word2id

# データ読み込み

train_data = load_sst_data("SST-2/train.tsv", word2id)
dev_data = load_sst_data("SST-2/dev.tsv", word2id)

# モデル準備

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

model = BoWClassifier(embedding).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# DataLoader 定義

train_loader = DataLoader(
    train_data,
    batch_size=32,
    shuffle=True,
    collate_fn=collate_batch
)

# 学習ループ

n_epochs = 5

for epoch in range(n_epochs):
    model.train()
    total_loss = 0.0

    for input_ids, labels in tqdm(train_loader, desc=f"Epoch {epoch+1}"):
        input_ids = input_ids.to(device)
        labels = labels.to(device)

        optimizer.zero_grad()
        logits = model(input_ids)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"[Epoch {epoch+1}] Average Loss: {avg_loss:.4f}")

# 評価

model.eval()
with torch.no_grad():
    dev_batch = collate_batch(dev_data)
    input_ids = dev_batch[0].to(device)
    labels = dev_batch[1].to(device)

    logits = model(input_ids)
    predictions = (torch.sigmoid(logits) >= 0.5).float()
    accuracy = (predictions == labels).float().mean()
    print(f"Validation Accuracy: {accuracy.item():.4f}")
