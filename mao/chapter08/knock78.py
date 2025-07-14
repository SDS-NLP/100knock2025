"""
knock78:単語埋め込みのファインチューニング
問題77の学習において、単語埋め込みのパラメータも同時に更新する
ファインチューニングを導入せよ。
また、学習したモデルの開発セットにおける正解率を求めよ。
"""
"""
knock78: 単語埋め込みのファインチューニング
問題77のモデル学習において、単語埋め込みも更新するように変更せよ。
"""

import torch
from torch import nn
from torch.utils.data import DataLoader
from knock71 import train_data, dev_data
from knock72 import BoWClassifier
from knock75 import collate
from tqdm import tqdm

# --- GPU 確認 ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"✅ Using device: {device}")

# --- embedding_matrix をファインチューニング可能にする ---
from knock70 import embedding_matrix
import torch.nn.functional as F

embedding_layer = nn.Embedding.from_pretrained(
    torch.tensor(embedding_matrix, dtype=torch.float32),
    freeze=False  # ← freeze=False にしてファインチューニングを許可
)

# --- モデルの再定義（embedding_layer を渡す形に変更） ---
class FineTuneBoWClassifier(nn.Module):
    def __init__(self, embedding_layer):
        super().__init__()
        self.embedding = embedding_layer
        self.linear = nn.Linear(embedding_layer.embedding_dim, 1)

    def forward(self, input_ids):
        embedded = self.embedding(input_ids)
        mean_embedded = embedded.mean(dim=1)  # BoW: 平均プーリング
        output = self.linear(mean_embedded).squeeze(1)
        return output

# --- モデル・損失関数・最適化 ---
model = FineTuneBoWClassifier(embedding_layer).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# --- データローダ ---
train_loader = DataLoader(train_data, batch_size=64, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(dev_data, batch_size=64, shuffle=False, collate_fn=collate)

# --- 学習ループ ---
for epoch in range(1, 6):
    model.train()
    total_loss = 0.0

    for batch in tqdm(train_loader, desc=f"Epoch {epoch}"):
        input_ids = batch['input_ids'].to(device)
        labels = batch['label'].to(device).squeeze()

        optimizer.zero_grad()
        logits = model(input_ids)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f"▶️ Epoch {epoch} - Training Loss: {avg_loss:.4f}")

# --- 評価関数 ---
def evaluate(model, dataloader):
    model.eval()
    correct = 0
    total = 0

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch['input_ids'].to(device)
            labels = batch['label'].to(device).squeeze()
            logits = model(input_ids)
            preds = (torch.sigmoid(logits) >= 0.5).float()
            correct += (preds == labels).sum().item()
            total += labels.size(0)

    return correct / total

# --- 開発セット評価 ---
dev_accuracy = evaluate(model, dev_loader)
print(f"✅ 開発セットの正解率（fine-tuned）: {dev_accuracy:.4f}")
