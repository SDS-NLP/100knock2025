import torch
import numpy as np
from knock73 import get_model_and_utils, load_sst_data

# モジュールから import
BoWClassifier, embedding, collate_batch, word2id = get_model_and_utils()

# モデル初期化
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = BoWClassifier(embedding).to(device)

# 学習済みパラメータをロード
model.load_state_dict(torch.load("model.pt"))


# dev data を読み込み
dev_data = load_sst_data("SST-2/dev.tsv", word2id)

# 評価
model.eval()
with torch.no_grad():
    input_ids, labels = collate_batch(dev_data)
    input_ids = input_ids.to(device)
    labels = labels.to(device)
    logits = model(input_ids)
    predictions = (torch.sigmoid(logits) >= 0.5).float()
    accuracy = (predictions == labels).float().mean()
    print(f"Validation Accuracy: {accuracy.item():.4f}")

# 出力
# Validation Accuracy: 0.7970