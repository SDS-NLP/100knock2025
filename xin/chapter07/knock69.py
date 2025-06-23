import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from knock63 import train_labels, train_dicts, dev_dicts, dev_labels

# ベクトル化
vectorizer = DictVectorizer()
X_train = vectorizer.fit_transform(train_dicts)
X_dev = vectorizer.transform(dev_dicts)

# 正則化パラメータ（対数スケールで幅広く試す）
C_values = np.logspace(-4, 2, 10)  # 10個：10^-4 ～ 10^2
accuracies = []

# 各Cについて学習・評価
for C in C_values:
    clf = LogisticRegression(C=C, max_iter=1000)
    clf.fit(X_train, train_labels)
    pred = clf.predict(X_dev)
    acc = accuracy_score(dev_labels, pred)
    accuracies.append(acc)

# グラフ描画
plt.figure(figsize=(8, 5))
plt.plot(C_values, accuracies, marker='o')
plt.xscale('log')  # Cはlogスケールで表示
plt.xlabel('Regularization Parameter C (log scale)')
plt.ylabel('Accuracy on Dev Set')
plt.title('Validation Accuracy vs Regularization Strength')
plt.grid(True)
plt.tight_layout()
plt.savefig('knock69_accuracy_vs_C.png', dpi=300)
