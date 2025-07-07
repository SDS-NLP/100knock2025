# 遅すぎて動かない gpuが必要
import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import pickle
from tqdm import tqdm
from knock73 import collate_batch, load_sst_data, word2id

# データ読み込み

train_data = load_sst_data("SST-2/train.tsv", word2id)
dev_data = load_sst_data("SST-2/dev.tsv", word2id)

# Embedding 準備

embedding_matrix = np.load("embedding_matrix.npy")
embedding_matrix = torch.tensor(embedding_matrix, dtype=torch.float32)

# freeze=False → 埋め込みを更新する
embedding = nn.Embedding.from_pretrained(
    embedding_matrix,
    freeze=False
)

# CNNモデル定義

class CNNClassifier(nn.Module):
    def __init__(self, embedding, num_filters=100, kernel_size=3):
        super().__init__()
        self.embedding = embedding
        self.conv = nn.Conv1d(
            in_channels=embedding.embedding_dim,
            out_channels=num_filters,
            kernel_size=kernel_size,
            padding=1      # same padding
        )
        self.relu = nn.ReLU()
        self.fc = nn.Linear(num_filters, 1)

    def forward(self, input_ids):
        # input_ids: [B, T]
        embedded = self.embedding(input_ids)           # [B, T, D]
        embedded = embedded.transpose(1, 2)            # [B, D, T]
        conv_out = self.conv(embedded)                 # [B, F, T]
        pooled = torch.max(conv_out, dim=2)[0]         # [B, F]
        x = self.relu(pooled)                          # [B, F]
        output = self.fc(x).squeeze(1)                 # [B]
        return output

# 学習準備

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

model = CNNClassifier(embedding).to(device)
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
