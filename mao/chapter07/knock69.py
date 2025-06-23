"""
knock69:正則化パラメータの変更
ロジスティック回帰モデルを学習するとき、正則化の係数（ハイパーパラメータ）を
調整することで、学習時の適合度合いを制御できる。
正則化の係数を変化させながらロジスティック回帰モデルを学習し、
検証データ上の正解率を求めよ。
実験の結果は、正則化パラメータを横軸、正解率を縦軸としたグラフにまとめよ。
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from knock61 import train_bow, dev_bow
from sklearn.feature_extraction import DictVectorizer

# データ準備
train_features = [d['feature'] for d in train_bow]
train_labels = [int(d['label']) for d in train_bow]
dev_features = [d['feature'] for d in dev_bow]
dev_labels = [int(d['label']) for d in dev_bow]

# 特徴ベクトルの変換
vectorizer = DictVectorizer(sparse=True)
X_train = vectorizer.fit_transform(train_features)
X_dev = vectorizer.transform(dev_features)
y_train = train_labels
y_dev = dev_labels

# 正則化パラメータ（Cは逆数: 小さいほど強い正則化）
C_values = np.logspace(-4, 4, 20)
accuracies = []

# 各Cで学習と評価
for C in C_values:
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_dev)
    acc = accuracy_score(y_dev, y_pred)
    accuracies.append(acc)

# グラフ描画
plt.figure(figsize=(10, 6))
plt.semilogx(C_values, accuracies, marker='o')
plt.xlabel("Regularization Parameter (C)")
plt.ylabel("Accuracy on Dev Data")
plt.title("Accuracy vs Regularization Parameter (C)")
plt.grid(True)
plt.tight_layout()
plt.show()
