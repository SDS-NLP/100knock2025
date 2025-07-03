import torch.nn as nn
import torch
from torch.utils.data import DataLoader, Dataset
from sklearn.metrics import accuracy_score
from knock73 import SSTDataset, collate_fn, compute_avg_embedding, embedding_tensor, train_loader
from knock74 import dev_loader, evaluate

# ここでは、SSTデータセットを使ったMLP分類器の学習と評価を行います。
# 1. MLPClassifierの定義
class MLPClassifier(nn.Module):
    def __init__(self, embedding_dim, hidden_dim=128):
        super(MLPClassifier, self).__init__()
        self.net = nn.Sequential(
            nn.Linear(embedding_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, 1)  # 最終出力は1次元（2値分類）
        )

    def forward(self, x):
        return self.net(x).squeeze(1)

# 2. DataLoaderの準備
model = MLPClassifier(embedding_dim=embedding_tensor.shape[1])
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

num_epochs = 10
model.train()

# 3. 学習ループ
for epoch in range(num_epochs):
    total_loss = 0
    for batch in train_loader:
        input_ids = batch["input_ids"]
        labels = batch["label"].squeeze(1)

        avg_emb = compute_avg_embedding(input_ids, embedding_tensor)
        logits = model(avg_emb)
        loss = criterion(logits, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
    print(f"[Epoch {epoch+1}] Loss: {total_loss / len(train_loader):.4f}")

# 4. 評価
evaluate(model.eval(), dev_loader, embedding_tensor)
