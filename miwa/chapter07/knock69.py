#69. 正則化パラメータの変更
from knock61 import train_data, dev_data
from knock62 import vectorizer, label_encoder
import matplotlib.pyplot as plt
import japanize_matplotlib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
japanize_matplotlib.japanize()

# 正則化パラメータのリスト（Cが小さいほど強い正則化）
C_values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]
accuracies = []

# データ準備
X_train = vectorizer.transform([ex['feature'] for ex in train_data])
y_train = label_encoder.transform([ex['label'] for ex in train_data])

X_dev = vectorizer.transform([ex['feature'] for ex in dev_data])
y_dev = label_encoder.transform([ex['label'] for ex in dev_data])

# 各Cに対して学習＆評価
for C in C_values:
    clf = LogisticRegression(C=C, max_iter=1000)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_dev)
    acc = accuracy_score(y_dev, y_pred)
    accuracies.append(acc)
    print(f"C={C:.3f} → Accuracy={acc:.4f}")

# グラフ表示
plt.figure(figsize=(8, 5))
plt.plot(C_values, accuracies, marker='o')
plt.xscale('log')
plt.xlabel("正則化パラメータ C（対数スケール）")
plt.ylabel("検証データの正解率")
plt.title("正則化パラメータと検証正解率の関係")
plt.grid(True)
plt.savefig("c_values")
