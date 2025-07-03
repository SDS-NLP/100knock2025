from torch.utils.data import DataLoader
from sklearn.metrics import accuracy_score
from knock72 import SSTDataset,collate_fn, compute_avg_embedding, BoWLogisticRegression, embedding_tensor
from knock71 import dev_data 
import torch
import torch.nn as nn

# 1. dev_data を DataLoader に変換
dev_dataset = SSTDataset(dev_data)
dev_loader = DataLoader(dev_dataset, batch_size=32, collate_fn=collate_fn)

# 2. 評価関数を定義
def evaluate(model, dataloader, embedding_tensor):
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for batch in dataloader:
            input_ids = batch["input_ids"]
            labels = batch["label"].squeeze(1)

            # 3. BoW 平均ベクトルを取得
            avg_emb = compute_avg_embedding(input_ids, embedding_tensor)

            # 4. モデルの予測 → 確率に変換 → 0/1に二値化
            logits = model(avg_emb)
            probs = torch.sigmoid(logits)
            preds = (probs > 0.5).long()

            # 5. 予測とラベルを集める
            all_preds.extend(preds.tolist())
            all_labels.extend(labels.tolist())

    # 6. Accuracy を計算して表示
    acc = accuracy_score(all_labels, all_preds)
    print(f"Development Set Accuracy: {acc:.4f}")

    model.train()  # 忘れずに train モードに戻す

import gensim.downloader as api
model=api.load("glove-wiki-gigaword-100")  # 100次元のGloVe埋め込みをロード
model = BoWLogisticRegression(embedding_dim=embedding_tensor.shape[1])
model.eval()  # 推論モードに切り替え


# 7. 評価実行
evaluate(model, dev_loader, embedding_tensor)
