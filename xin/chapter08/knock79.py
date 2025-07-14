import torch.nn as nn
import torch
from knock73 import  compute_avg_embedding, embedding_tensor, train_loader
from knock74 import dev_loader, evaluate

# ここでは、MLP分類器(多層パーセプトロン)の学習と評価を行います。
# 1. MLPClassifierの定義
class MLPClassifier(nn.Module):
    def __init__(self, embedding_dim, hidden_dim=128):
        super(MLPClassifier, self).__init__() #親クラスの初期化
        self.net = nn.Sequential(
            nn.Linear(embedding_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, 1)  # 最終出力は1次元（2値分類）
        )
        #embedding_dimは入力ベクトルの次元数（単語埋め込みの次元）、hidden_dimは中間層のノード数。
        #nn.Linearは入力層から隠れ層（128層）、
        #nn.ReLUは活性化関数、
        #nn.Dropoutは過学習防止のため学習時にニューロンを30％の確率で無効化。
        #nn.Linearは隠れ層から出力層（1次元）への線形変換を行う。

    def forward(self, x):
        return self.net(x).squeeze(1)
    #最終出力が (バッチサイズ, 1) になっているので squeeze(1) で (バッチサイズ,) に。

# 2. DataLoaderの準備
model = MLPClassifier(embedding_dim=embedding_tensor.shape[1]) #embedding_tensor は 語彙数 × 埋め込み次元 の行列。
criterion = nn.BCEWithLogitsLoss()                             # バイナリ分類のための損失関数
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)      #モデルのパラメータを更新する

num_epochs = 10
model.train() # モデルを学習モードに設定

# 3. 学習ループ
for epoch in range(num_epochs):
    total_loss = 0
    for batch in train_loader:            #train_loader は、辞書型のミニバッチを返す DataLoader。
        input_ids = batch["input_ids"]    # ミニバッチの入力ID 
        labels = batch["label"].squeeze(1)# ミニバッチのラベル（1次元に変形）

        avg_emb = compute_avg_embedding(input_ids, embedding_tensor) # どんな長さの文も、同じ長さのベクトルで表現できるように
        logits = model(avg_emb)                                      # モデルに平均埋め込みベクトルを入力してロジットを取得
        loss = criterion(logits, labels)                             # ロジットとラベルを使って損失を計算

        optimizer.zero_grad()# 勾配を初期化
        loss.backward()      # 勾配を計算
        optimizer.step()     # パラメータを更新

        total_loss += loss.item()
    print(f"[Epoch {epoch+1}] Loss: {total_loss / len(train_loader):.4f}")

# 4. 評価
evaluate(model.eval(), dev_loader, embedding_tensor) #モデルを評価モードに設定し、dev_loaderを使って評価を行う
