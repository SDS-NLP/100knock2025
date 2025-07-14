"""
knock79:アーキテクチャの変更
ニューラルネットワークのアーキテクチャを自由に変更し、モデルを学習せよ。
また、学習したモデルの開発セットにおける正解率を求めよ。
例えば、テキストの特徴ベクトル（単語埋め込みの平均ベクトル）に対して
多層のニューラルネットワークを通したり、畳み込みニューラルネットワーク（CNN; Convolutional Neural Network）
や再帰型ニューラルネットワーク（RNN; Recurrent Neural Network）などの
モデルの学習に挑戦するとよい。
"""
"""
knock79: アーキテクチャの変更
MLP（多層パーセプトロン）構造を導入し、BoW 平均ベクトルを通じて分類を行う。
"""

import torch
from torch import nn
from torch.utils.data import DataLoader
from knock70 import embedding_matrix
from knock71 import train_data, dev_data
from knock75 import collate
from tqdm import tqdm

# --- デバイス設定 ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"✅ Using device: {device}")

# --- 埋め込み層（ファインチューニング可） ---
embedding_layer = nn.Embedding.from_pretrained(
    torch.tensor(embedding_matrix, dtype=torch.float32),
    freeze=False
)

# --- MLPによるBoW分類器 ---
class MLPClassifier(nn.Module):
    def __init__(self, embedding_layer):
        super().__init__()
        self.embedding = embedding_layer
        self.classifier = nn.Sequential(
            nn.Linear(embedding_layer.embedding_dim, 128),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(64, 1)  # 出力1次元（BCEWithLogitsLoss用）
        )

    def forward(self, input_ids):
        emb = self.embedding(input_ids)       # (B, T, D)
        mean_emb = emb.mean(dim=1)            # (B, D)
        return self.classifier(mean_emb).squeeze(1)  # (B,)

# --- モデル・損失・最適化設定 ---
model = MLPClassifier(embedding_layer).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# --- データローダ ---
train_loader = DataLoader(train_data, batch_size=64, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(dev_data, batch_size=64, shuffle=False, collate_fn=collate)

# --- 学習ループ ---
def train(model, loader):
    model.train()
    total_loss = 0.0
    for batch in tqdm(loader, desc="Training"):
        x = batch['input_ids'].to(device)
        y = batch['label'].to(device).squeeze()
        optimizer.zero_grad()
        logits = model(x)
        loss = criterion(logits, y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    return total_loss / len(loader)

# --- 評価関数 ---
def evaluate(model, loader):
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for batch in loader:
            x = batch['input_ids'].to(device)
            y = batch['label'].to(device).squeeze()
            logits = model(x)
            preds = (torch.sigmoid(logits) >= 0.5).float()
            correct += (preds == y).sum().item()
            total += y.size(0)
    return correct / total

# --- 実行 ---
for epoch in range(1, 6):
    loss = train(model, train_loader)
    acc = evaluate(model, dev_loader)
    print(f"[Epoch {epoch}] Loss: {loss:.4f} | Dev Accuracy: {acc:.4f}")
