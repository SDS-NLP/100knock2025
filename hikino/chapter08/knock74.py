from knock70 import embedding_dim
from knock72 import LogisticRegressionClassifier, X_dev, y_dev
import torch
import torch.nn as nn



model = LogisticRegressionClassifier(input_dim=embedding_dim)
model.load_state_dict(torch.load("model.pth"))
model.eval()

# --- 評価（推論モード）
with torch.no_grad():
    outputs = model(X_dev).squeeze()
    preds = (outputs >= 0.5).float()
    accuracy = (preds == y_dev.squeeze()).float().mean()

print(f"Dev Accuracy: {accuracy:.4f}")