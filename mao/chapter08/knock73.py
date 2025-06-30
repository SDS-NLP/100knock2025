"""
knock73:モデルの学習
問題72で設計したモデルの重みベクトルを訓練セット上で学習せよ。
ただし、学習中は単語埋め込み行列の値を固定せよ
（単語埋め込み行列のファインチューニングは行わない）。
また、学習時に損失値を表示するなど、学習の進捗状況をモニタリングできるようにせよ。
"""
import torch
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from torch import nn
from tqdm import tqdm
from knock70 import embedding_matrix
from knock71 import train_data
from knock72 import BoWClassifier

# --- モデルと学習準備 ---
model = BoWClassifier(embedding_matrix)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

# --- データローダ準備（パディング処理付き） ---
def collate_fn(batch):
    input_ids = [item['input_ids'] for item in batch]
    labels = torch.cat([item['label'] for item in batch])  # (batch_size,)
    input_ids = pad_sequence(input_ids, batch_first=True, padding_value=0)
    return input_ids, labels

train_loader = DataLoader(train_data, batch_size=64, shuffle=True, collate_fn=collate_fn)

# --- 学習ループ ---
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

for epoch in range(1, 51):  # 11エポック
    model.train()
    total_loss = 0.0

    for input_ids, labels in tqdm(train_loader, desc=f'Epoch {epoch}'):
        input_ids, labels = input_ids.to(device), labels.to(device)

        optimizer.zero_grad()
        logits = model(input_ids)
        loss = criterion(logits, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_loss = total_loss / len(train_loader)
    print(f'▶️ Epoch {epoch} - Loss: {avg_loss:.4f}')
