from knock62 import model, X_dev, y_dev
import numpy as np

# モデルの予測確率を取得
probabilities = model.predict_proba(X_dev[:1])

# 出力の整形
labels = model.classes_
for label, prob in zip(labels, probabilities[0]):
    print(f"Label: {label}, Conditional Probability: {prob:.4f}")

#Label: 0, Conditional Probability: 0.0043
#Label: 1, Conditional Probability: 0.9957