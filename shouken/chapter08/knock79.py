import torch
from torch import nn, optim
from torch.utils.data import DataLoader
from knock71 import train_dataset, dev_dataset
from knock70 import embedding_matrix
from knock75 import collate

# アーキテクチャ：MLPモデル（1中間層 + ReLU + Dropout）
class MLPClassifier(nn.Module):
    def __init__(self, embedding_matrix, hidden_dim=128, dropout_rate=0.3):
        super().__init__()
        vocab_size, embedding_dim = embedding_matrix.shape
        self.embedding = nn.Embedding.from_pretrained(
            embeddings=torch.tensor(embedding_matrix, dtype=torch.float32),
            freeze=False  # ファインチューニング可
        )
        self.dropout = nn.Dropout(dropout_rate)
        self.fc1 = nn.Linear(embedding_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(hidden_dim, 1)
        self.sigmoid = nn.Sigmoid()

    def forward(self, input_ids):
        embedded = self.embedding(input_ids)               # (batch, seq_len, dim)
        mean_vector = embedded.mean(dim=1)                 # (batch, dim)
        x = self.dropout(mean_vector)
        x = self.relu(self.fc1(x))                         # (batch, hidden)
        logits = self.fc2(x)                               # (batch, 1)
        return self.sigmoid(logits)

# 設定
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
batch_size = 32
num_epochs = 5
lr = 1e-3

print(f"使用デバイス: {device}")

# Dataset wrapper
class SSTDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx]

# DataLoader
train_loader = DataLoader(SSTDataset(train_dataset), batch_size=batch_size, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(SSTDataset(dev_dataset), batch_size=batch_size, shuffle=False, collate_fn=collate)

# モデル・損失・最適化
model = MLPClassifier(embedding_matrix).to(device)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=lr)

# 学習
for epoch in range(1, num_epochs + 1):
    model.train()
    total_loss = 0
    for batch in train_loader:
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device)

        optimizer.zero_grad()
        outputs = model(input_ids)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"[Epoch {epoch}] 損失: {total_loss / len(train_loader):.4f}")

# 評価
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for batch in dev_loader:
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device)
        outputs = model(input_ids)
        preds = (outputs >= 0.5).float()
        correct += (preds == labels).sum().item()
        total += labels.size(0)

accuracy = correct / total
print(f"\n[評価] 開発セットの正解率: {accuracy:.4f}")
