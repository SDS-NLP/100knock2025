#74. モデルの評価
import torch
from knock73 import model, train_model, evaluate, train_loader, dev_loader

train_model(model, train_loader, dev_loader, epochs=10, lr=1e-3)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
accuracy = evaluate(model, dev_loader, device)
print(f"開発セットの正解率: {accuracy:.4f}")