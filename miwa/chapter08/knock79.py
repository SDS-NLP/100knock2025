#79. アーキテクチャの変更

#以下のプログラムをGoogle Colab上で実装

#!pip install gensim

import torch
import torch.nn as nn
import torch.optim as optim
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import DataLoader, Dataset
from gensim.models import KeyedVectors
import numpy as np
import csv

#70
embedding_path = "/content/GoogleNews-vectors-negative300.bin.gz"

print("Word2Vecモデルを読み込み")
model = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
print("モデル読み込み完了")

d_emb = model.vector_size  # 埋め込みの次元（GoogleNewsは300）
word2id = {'<PAD>': 0}  #語彙→idに変換できる辞書、<PAD>のidを0に設定
id2word = {0: '<PAD>'}  #id→語彙に変換できる辞書、id0は<PAD>
embedding_vectors = [np.zeros(d_emb, dtype=np.float32)]  # E[0] ← ゼロベクトル


# 語彙を順番に追加（max_vocab_size で制限）
max_vocab_size=50000 #語彙数制限　全部取り出したら多すぎるから
for i, word in enumerate(model.index_to_key): #model.index_to_keyで語彙を出現頻度順に取り出す
    if max_vocab_size and len(word2id) >= max_vocab_size:
        break
    vector = model[word]
    idx = len(word2id)
    word2id[word] = idx
    id2word[idx] = word
    embedding_vectors.append(vector)

#リスト形式のembeddig_vectorsから二次元の行列を作る
E = np.vstack(embedding_vectors)

#71
def load_sst_dataset(file_path, word2id):
    dataset = []

    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        next(reader)  # ヘッダーをスキップ

        for line in reader:
            if len(line) != 2:
                continue  # 空行・不正行スキップ

            text, label_str = line
            tokens = text.strip().split()
            
            # 単語埋め込み語彙に含まれる単語だけで input_ids を作成
            input_ids = [word2id[word] for word in tokens if word in word2id]

            if len(input_ids) == 0:
                continue  # 空なら除外

            label = torch.tensor([float(label_str)], dtype=torch.float32) #テンソル＝多次元の数値配列（スカラー、ベクトル、行列の総称）　ニューラルネットワークの入出力はすべてテンソルなので、変換する

            dataset.append({
                'text': text,
                'label': label,
                'input_ids': torch.tensor(input_ids, dtype=torch.long)
            })

    print(f"読み込み済み: {file_path}, 有効な事例数: {len(dataset)}")
    return dataset

train_dataset = load_sst_dataset("/content/train.tsv", word2id)
dev_dataset = load_sst_dataset("/content/dev.tsv", word2id)

# 1件確認
print(train_dataset[0])

#75
def collate(batch):
    #トークンの長さで長い順にソート
    batch.sort(key=lambda x: len(x["input_ids"]), reverse = True)

    #各項目をまとめて取得
    input_ids = [item["input_ids"] for item in batch]
    labels = [item["label"] for item in batch]

    #パディング
    padded_input_ids = pad_sequence(input_ids, batch_first=True, padding_value=0)
    #ラベルも一つのテンソルにする
    label_tensor = torch.stack(labels)

    return {
        "input_ids" : padded_input_ids, #(バッチ数, 最大長)
        "label" : label_tensor #(バッチ数, 1)
    }

#試してみる
example = train_dataset[:4]
print(collate(example))

class SSTBoWDataset(Dataset):
    def __init__(self, loaded_dataset):
        self.data = loaded_dataset

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
      input_ids = self.data[idx]["input_ids"]
      if isinstance(input_ids, torch.Tensor):
          input_ids = input_ids.clone().detach()
      else:
          input_ids = torch.tensor(input_ids, dtype=torch.long)

      label = self.data[idx]["label"]
      label = torch.tensor([label], dtype=torch.float)

      return {
          "input_ids": input_ids,
          "label": label
      }
    
#多層ニューラルネットワークに変更
# 隠れ層を二層追加する。線形変換と非線形変換（ReLU）

class MLPClassifier(nn.Module):
    def __init__(self, embedding_layer, hidden_dim1=128, hidden_dim2=64, dropout=0.3):
        super().__init__()
        self.embedding = embedding_layer
        d_emb = self.embedding.embedding_dim

        self.fc1 = nn.Linear(d_emb, hidden_dim1)
        self.fc2 = nn.Linear(hidden_dim1, hidden_dim2)
        self.fc_out = nn.Linear(hidden_dim2, 1)

        self.relu = nn.ReLU()
        self.dropout = nn.Dropout(dropout)

    def forward(self, input_ids):
        emb = self.embedding(input_ids)      # (B, L, D)
        emb_mean = emb.mean(dim=1)           # (B, D)

        x = self.dropout(self.relu(self.fc1(emb_mean)))  # (B, H1)
        x = self.dropout(self.relu(self.fc2(x)))          # (B, H2)
        x = self.fc_out(x)                                # (B, 1)
        return torch.sigmoid(x).squeeze(1)                # (B,)


def evaluate(model, data_loader, device):
    model.eval()
    correct = 0
    total = 0
    with torch.no_grad():
        for batch in data_loader:
            input_ids = batch["input_ids"].to(device)
            labels = batch["label"].to(device).squeeze(1)

            preds = model(input_ids)
            predicted = (preds >= 0.5).float()
            correct += (predicted == labels).sum().item()
            total += labels.size(0)
    return correct / total

def train_model(model, train_loader, dev_loader, epochs=5, lr=1e-3):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    optimizer = optim.Adam(model.parameters(), lr=lr)
    criterion = nn.BCELoss()

    for epoch in range(1, epochs + 1):
        model.train()
        total_loss = 0

        for batch in train_loader:
            input_ids = batch["input_ids"].to(device)  
            labels = batch["label"].to(device).squeeze(1)

            optimizer.zero_grad()
            preds = model(input_ids)
            loss = criterion(preds, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        acc = evaluate(model, dev_loader, device)
        print(f"Epoch {epoch}: Loss={total_loss:.4f}, Dev Accuracy={acc:.4f}")

train_dataset = SSTBoWDataset(train_dataset)
dev_dataset = SSTBoWDataset(dev_dataset)

train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate)
dev_loader = DataLoader(dev_dataset, batch_size=32, collate_fn=collate)

embedding_layer = nn.Embedding.from_pretrained(
    torch.tensor(E, dtype=torch.float32),
    freeze=False  # ← ファインチューニング可能にする
)

model = MLPClassifier(embedding_layer)
train_model(model, train_loader, dev_loader, epochs=10, lr=1e-3)
"""

出力結果
Epoch 1: Loss=707.4964, Dev Accuracy=0.8085
Epoch 2: Loss=484.7214, Dev Accuracy=0.7901
Epoch 3: Loss=400.7926, Dev Accuracy=0.8016
Epoch 4: Loss=341.6590, Dev Accuracy=0.7810
Epoch 5: Loss=304.9239, Dev Accuracy=0.7890
Epoch 6: Loss=276.0549, Dev Accuracy=0.7844
Epoch 7: Loss=254.3576, Dev Accuracy=0.8016
Epoch 8: Loss=234.3531, Dev Accuracy=0.7844
Epoch 9: Loss=221.6572, Dev Accuracy=0.7787
Epoch 10: Loss=206.5264, Dev Accuracy=0.7844
ちょっと上振れするようになった、というくらい？
"""