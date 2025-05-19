from knock62 import model, X_dev, y_dev
from sklearn.metrics import accuracy_score

y_pred = model.predict(X_dev)
accuracy = accuracy_score(y_dev, y_pred)

print(f"検証精度（Accuracy）: {accuracy:.4f}")