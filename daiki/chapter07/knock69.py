from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import joblib
from knock61 import train_examples, dev_examples

# データ準備
X_train_dict = [ex["feature"] for ex in train_examples]
y_train = [int(ex["label"]) for ex in train_examples]
X_dev_dict = [ex["feature"] for ex in dev_examples]
y_dev = [int(ex["label"]) for ex in dev_examples]

# ベクトライザの読み込み
_, vectorizer = joblib.load("logistic_model.joblib")
X_train = vectorizer.transform(X_train_dict)
X_dev = vectorizer.transform(X_dev_dict)

# 正則化パラメータのリスト
C_values = [0.01, 0.1, 1, 10, 100]
accuracies = []

# Cごとに学習・評価
for C in C_values:
    model = LogisticRegression(max_iter=300, C=C, solver='liblinear')
    model.fit(X_train, y_train)
    y_pred = model.predict(X_dev)
    acc = accuracy_score(y_dev, y_pred)
    print(f"C={C}: accuracy={acc:.4f}")
    accuracies.append(acc)

# グラフ描画
plt.plot(C_values, accuracies, marker='o')
plt.xscale('log')
plt.xlabel("Regularization parameter (C)")
plt.ylabel("Accuracy on dev set")
plt.title("Effect of Regularization on Accuracy")
plt.grid(True)
plt.tight_layout()
plt.show()
