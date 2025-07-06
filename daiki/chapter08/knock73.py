import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
import pickle
from tqdm import tqdm



# 準備済みファイルの読み込み

# 埋め込み行列
embedding_matrix = np.load("embedding_matrix.npy")
embedding_matrix = torch.tensor(embedding_matrix, dtype=torch.float32)

# word2id
with open("word2id.pkl", "rb") as f:
    word2id = pickle.load(f)

def load_sst_data(tsv_path, word2id):
    dataset = []
    with open(tsv_path, encoding="utf-8") as f:
        next(f)  # ヘッダーをスキップ
        for line in f:
            try:
                text, label = line.strip().split("\t")
                tokens = text.split()  # 単語分割（空白区切り）
                input_ids = [word2id[token] for token in tokens if token in word2id]
                if not input_ids:
                    continue  # 空のトークン列は除外
                ex = {
                    "text": text,
                    "label": torch.tensor([float(label)]),
                    "input_ids": torch.tensor(input_ids)
                }
                dataset.append(ex)
            except ValueError:
                continue  # 不正な行があればスキップ
    return dataset

# この位置で呼び出す
train_data = load_sst_data("SST-2/train.tsv", word2id)
dev_data = load_sst_data("SST-2/dev.tsv", word2id)


# collate_fn 定義

def collate_batch(batch):
    input_ids = [ex["input_ids"] for ex in batch]
    labels = [ex["label"] for ex in batch]
    input_ids = nn.utils.rnn.pad_sequence(input_ids, batch_first=True, padding_value=0)
    labels = torch.cat(labels)
    return input_ids, labels

# モデル定義

# freeze=True → 埋め込みを更新しない
embedding = nn.Embedding.from_pretrained(embedding_matrix, freeze=True)

class BoWClassifier(nn.Module):
    def __init__(self, embedding):
        super().__init__()
        self.embedding = embedding
        self.linear = nn.Linear(embedding.embedding_dim, 1)

    def forward(self, input_ids):
        embedded = self.embedding(input_ids)         # [B, T, D]
        mask = (input_ids != 0).unsqueeze(-1)         # [B, T, 1]
        summed = (embedded * mask).sum(dim=1)         # [B, D]
        lengths = mask.sum(dim=1).clamp(min=1)        # avoid div by zero
        averaged = summed / lengths                   # [B, D]
        output = self.linear(averaged).squeeze(1)     # [B]
        return output

# 学習

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

model = BoWClassifier(embedding).to(device)
criterion = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

train_loader = DataLoader(
    train_data, batch_size=32, shuffle=True, collate_fn=collate_batch
)

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

# モデルを保存
torch.save(model.state_dict(), "model.pt")


# モデルクラスと embedding, collate 関数を export する
def get_model_and_utils():
    return BoWClassifier, embedding, collate_batch, word2id