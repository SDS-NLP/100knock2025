import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from knock62 import X_train, y_train, X_dev, y_dev

# 正則化パラメータの候補（logスケールで広くカバー）
C_values = np.logspace(-4, 4, 20)
accuracies = []

# 各Cでモデルを学習し、検証データで精度を測定
for C in C_values:
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_dev)
    acc = accuracy_score(y_dev, y_pred)
    accuracies.append(acc)

# グラフ表示
plt.figure(figsize=(8, 5))
plt.plot(C_values, accuracies, marker='o')
plt.xscale('log')
plt.xlabel('parameters C（log scale）')
plt.ylabel('accuracy')
plt.title('Regularization')
plt.grid(True)
plt.tight_layout()
plt.savefig("../../../seisokuka.png")
