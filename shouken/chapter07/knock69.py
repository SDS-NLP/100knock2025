import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
from knock61 import train_data, dev_data  # 同じフォルダにあること

# データ整形
def extract_X_y(data):
    X = [d['feature'] for d in data]
    y = [int(d['label']) for d in data]
    return X, y

X_train, y_train = extract_X_y(train_data)
X_dev, y_dev = extract_X_y(dev_data)

# 正則化パラメータ（C）を変化させる（対数スケール）
C_values = [10**i for i in range(-4, 5)]  # 0.0001 ～ 10000
accuracies = []

for C in C_values:
    model = Pipeline([
        ('vectorizer', DictVectorizer()),
        ('classifier', LogisticRegression(C=C, max_iter=1000))
    ])
    model.fit(X_train, y_train)
    y_pred = model.predict(X_dev)
    acc = accuracy_score(y_dev, y_pred)
    accuracies.append(acc)

# グラフ描画
plt.figure(figsize=(8, 5))
plt.plot(C_values, accuracies, marker='o')
plt.xscale('log')
plt.xlabel('正則化パラメータ C（logスケール）')
plt.ylabel('検証データの正解率')
plt.title('正則化の強さとモデル精度の関係')
plt.grid(True)
plt.tight_layout()
plt.show()
