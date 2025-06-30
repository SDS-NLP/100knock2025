# 74. モデルの評価
# 問題73で学習したモデルの開発セットにおける正解率を求めよ。

# knock74.py
import torch
from torch.utils.data import DataLoader
from torch.nn.utils.rnn import pad_sequence
from knock71 import load_dataset
from knock72 import BoWClassifier

# -----------------------------
# ファイル・パラメータ設定
# -----------------------------
BATCH_SIZE = 64
word2id = torch.load("word2id.pt")
embedding_matrix = torch.load("embedding.pt")

# -----------------------------
# データ読み込み
# -----------------------------
dev_data = load_dataset("SST-2/dev.tsv", word2id)

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
# DataLoader 準備
# -----------------------------
dev_loader = DataLoader(dev_data, batch_size=BATCH_SIZE, shuffle=False, collate_fn=collate_fn)

# -----------------------------
# モデル読み込み
# -----------------------------
model = BoWClassifier(embedding_matrix)
model.load_state_dict(torch.load("bow_model.pt"))
model.eval()

# -----------------------------
# 評価ループ
# -----------------------------
correct = 0
total = 0

with torch.no_grad():
    for batch in dev_loader:
        inputs = batch["input_ids"]
        labels = batch["label"]
        outputs = model(inputs).squeeze()
        preds = (outputs >= 0.5).float()
        correct += (preds == labels).sum().item()
        total += labels.size(0)

accuracy = correct / total
print(f"✅ 開発セットの正解率: {accuracy:.4f}")

