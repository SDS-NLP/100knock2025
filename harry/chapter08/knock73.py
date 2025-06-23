# 73. モデルの学習
# 問題72で設計したモデルの重みベクトルを訓練セット上で学習せよ。
# ただし、学習中は単語埋め込み行列の値を固定せよ（単語埋め込み行列のファインチューニングは行わない）。
# また、学習時に損失値を表示するなど、学習の進捗状況をモニタリングできるようにせよ。

# knock73.py
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from knock71 import load_dataset
from knock72 import BoWClassifier

# -----------------------------
# ハイパーパラメータ
# -----------------------------
BATCH_SIZE = 64
NUM_EPOCHS = 5
LR = 0.01

# -----------------------------
# データと辞書の読み込み
# -----------------------------
word2id = torch.load("word2id.pt")
embedding_matrix = torch.load("embedding.pt")

train_data = load_dataset("SST-2/train.tsv", word2id)
dev_data = load_dataset("SST-2/dev.tsv", word2id)

print(f"✅ train.tsv: {len(train_data)} 件のデータを読み込みました")
print(f"✅ dev.tsv: {len(dev_data)} 件のデータを読み込みました")
print(f"📝 例： {train_data[0]}")

# -----------------------------
# モデル定義
# -----------------------------
model = BoWClassifier(embedding_matrix)
criterion = nn.BCELoss()
optimizer = optim.Adam(model.parameters(), lr=LR)

# -----------------------------
# collate関数（パディング処理）
# -----------------------------
def collate_fn(batch):
    texts = [item['text'] for item in batch]
    labels = torch.cat([item['label'] for item in batch])
    input_ids = [item['input_ids'] for item in batch]
    input_ids_padded = pad_sequence(input_ids, batch_first=True, padding_value=0)
    return {'text': texts, 'label': labels, 'input_ids': input_ids_padded}

# -----------------------------
# ミニバッチ用 DataLoader
# -----------------------------
train_loader = DataLoader(train_data, batch_size=BATCH_SIZE, shuffle=True, collate_fn=collate_fn)

# -----------------------------
# 学習ループ
# -----------------------------
model.train()
for epoch in range(NUM_EPOCHS):
    total_loss = 0.0
    for batch in train_loader:
        inputs = batch["input_ids"]
        labels = batch["label"]

        optimizer.zero_grad()
        outputs = model(inputs).squeeze()
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"📉 Epoch {epoch+1}: Loss = {total_loss:.4f}")

# -----------------------------
# モデル保存（任意）
# -----------------------------
torch.save(model.state_dict(), "bow_model.pt")



