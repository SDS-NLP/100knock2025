#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
from gensim.models import KeyedVectors
import numpy as np

# Word2Vec モデルの読み込み
# 事前学習済みの Google News の単語ベクトルを読み込む
w2v_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin" 
print("Loading Word2Vec model...")
w2v = KeyedVectors.load_word2vec_format(w2v_path, binary=True)
print("Loaded!")

# Word2Vec を embedding matrixに変換
def convert_w2v_to_embedding_matrix(w2v_model, max_vocab=50000):
    word2id = {'<PAD>': 0}  # パディング用トークン
    vectors = [np.zeros(w2v_model.vector_size)]  # <PAD> に対応するゼロベクトル
    for word in w2v_model.index_to_key[:max_vocab]:  # 最大語彙数まで取得
        word2id[word] = len(vectors)
        vectors.append(w2v_model[word])
    embedding_matrix = torch.tensor(np.array(vectors), dtype=torch.float32)
    id2word = {v: k for k, v in word2id.items()}
    return embedding_matrix, word2id, id2word

embedding_matrix, word2id, id2word = convert_w2v_to_embedding_matrix(w2v)
print("embedding_matrix 生成成功")

# BoW + ロジスティック回帰モデルの定義
class BoWLogRegModel(nn.Module):
    def __init__(self, embedding_matrix):
        super().__init__()
        # 埋め込み層：事前学習済みのベクトルを使用（freeze=True で学習しない）
        self.emb = nn.Embedding.from_pretrained(embedding_matrix, freeze=True)
        # 線形層（平均ベクトル → 1つの出力スコア）
        self.linear = nn.Linear(embedding_matrix.shape[1], 1)

    def forward(self, input_ids):
        emb = self.emb(input_ids)              # (batch_size, seq_len, 300)
        mean_emb = emb.mean(dim=1)             # BoW：単語ベクトルの平均をとる
        logits = self.linear(mean_emb)         # 線形変換
        probs = torch.sigmoid(logits)          # シグモイド関数で確率に変換
        return probs

# 訓練データの定義

words = ["phonology", "morphology", "syntax", "semantics", "cat", "dog", "fish", "bear"]
for word in words:
    if word in w2v:
        print(f"{word} ✅")
    else:
        print(f"{word} ❌")


# 2文の例文とそのラベル（1=ポジティブ、0=ネガティブ）
train_sentences = [
    ["phonology", "morphology", "syntax", "semantics"],
    ["cat", "dog", "fish", "bear"]
]
train_labels = [1, 0]

# 開発セット（検証用データ）の定義
dev_sentences = [
    ["phonological", "morphological", "syntactic", "semantic"],
    ["cats", "dogs", "fishes", "bears"]
]
dev_labels = [1, 0]

# 文 → 単語ID に変換（最大4語までパディング）
def encode(sentences, word2id, max_len=4):
    results = []
    for sent in sentences:
        ids = [word2id.get(w, 0) for w in sent]  # 語彙にない単語は0（<PAD>）で埋める
        ids += [0] * (max_len - len(ids))        # パディング
        results.append(ids)
    return torch.tensor(results, dtype=torch.long)

X_train = encode(train_sentences, word2id)
y_train = torch.tensor(train_labels, dtype=torch.float32).unsqueeze(1)

X_dev = encode(dev_sentences, word2id)
y_dev = torch.tensor(dev_labels, dtype=torch.float32).unsqueeze(1)

# モデルの訓練
model = BoWLogRegModel(embedding_matrix)               # モデルのインスタンス化
criterion = nn.BCELoss()                               # 損失関数：バイナリクロスエントロピー
optimizer = optim.Adam(filter(lambda p: p.requires_grad, model.parameters()), lr=0.001)

train_loader = DataLoader(TensorDataset(X_train, y_train), batch_size=2, shuffle=True)

EPOCHS = 10  # エポック数（繰り返し回数）
for epoch in range(EPOCHS):
    model.train()
    total_loss = 0.0
    for batch_x, batch_y in train_loader:
        optimizer.zero_grad()               # 勾配の初期化
        outputs = model(batch_x)            # モデルによる予測
        loss = criterion(outputs, batch_y)  # 損失の計算
        loss.backward()                     # 誤差逆伝播
        optimizer.step()                    # パラメータの更新
        total_loss += loss.item()           # バッチごとの損失を合計
    print(f"[Epoch {epoch+1}] Loss: {total_loss:.4f}")

#ここまでは73の内容 

# モデルの評価
model.eval()  # 評価モードに切り替え
with torch.no_grad():  # 勾配計算を無効化
    outputs = model(X_dev)                    # 検証データで予測
    preds = (outputs >= 0.5).float()          # 閾値0.5でクラス分類（0または1）
    correct = (preds == y_dev).sum().item()   # 正解した数をカウント
    total = y_dev.size(0)                     # 全体のデータ数
    acc = correct / total                     # 正解率を計算

print(f"開発セットの正解率（Accuracy）: {acc * 100:.2f}%")

