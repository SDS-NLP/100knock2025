#74. モデルの評価
import torch
from knock73 import model, evaluate, dev_loader

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
accuracy = evaluate(model, dev_loader, device)
print(f"開発セットの正解率: {accuracy:.4f}")