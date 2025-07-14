# knock78.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from knock71 import load_dataset
from knock75 import collate_fn

# -----------------------------
# ハイパーパラメータ
# -----------------------------
BATCH_SIZE = 64
NUM_EPOCHS = 5
LR = 0.01

# -----------------------------
# デバイスの設定
# -----------------------------
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"🚀 使用デバイス: {device}")

# -----------------------------
# データと辞書の読み込み
# -----------------------------
word2id = torch.load("word2id.pt")
embedding_matrix = torch.load("embedding.pt")

train_data = load_dataset("SST-2/train.tsv", word2id)
dev_data = load_dataset("SST-2/dev.tsv", word2id)

train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)
dev_loader = DataLoader(dev_data, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_fn)

# -----------------------------
# モデル定義（ファインチューニング有効）
# -----------------------------
class BoWClassifierFT(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        vocab_size, emb_dim = embedding_matrix.size()
        self.embedding = nn.Embedding.from_pretrained(embedding_matrix, freeze=False, padding_idx=0)  # freeze=False
        self.fc = nn.Linear(emb_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, input_ids):
        embedded = self.embedding(input_ids)
        mask = (input_ids != 0).unsqueeze(-1).float()
        summed = torch.sum(embedded * mask, dim=1)
        lengths = torch.sum(mask, dim=1) + 1e-9
        averaged = summed / lengths
        out = self.fc(averaged)
        return self.sigmoid(out)

# -----------------------------
# モデル・損失関数・最適化器
# -----------------------------
model = BoWClassifierFT(embedding_matrix).to(device)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# -----------------------------
# 学習ループ
# -----------------------------
model.train()
for epoch in range(NUM_EPOCHS):
    total_loss = 0.0
    for batch in train_loader:
        input_ids = batch["input_ids"].to(device)
        labels = batch["label"].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids).squeeze()
        loss = criterion(outputs, labels.squeeze())
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"📉 Epoch {epoch+1}: Loss = {total_loss:.4f}")

# -----------------------------
# 評価ループ
# -----------------------------
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for batch in dev_loader:
        input_ids = batch["input_ids"].to(device)
        labels = batch["label"].to(device)

        outputs = model(input_ids).squeeze()
        predictions = (outputs >= 0.5).float()
        correct += (predictions == labels.squeeze()).sum().item()
        total += labels.size(0)

accuracy = correct / total
print(f"✅ 開発セットの正解率（FTあり）: {accuracy:.4f}")
