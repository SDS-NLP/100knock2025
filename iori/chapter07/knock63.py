from knock62 import model, X_dev, y_dev

# モデルの評価
accuracy = model.score(X_dev, y_dev)
print(f"Accuracy: {accuracy:.4f}")
