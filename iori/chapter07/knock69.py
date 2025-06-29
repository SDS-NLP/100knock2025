import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

train = pd.read_csv('SST-2/train.tsv', sep='\t')
dev = pd.read_csv('SST-2/dev.tsv', sep='\t')

def text_to_feature(text):
    tokens = text.split()
    feature = {}
    for token in tokens:
        feature[token] = feature.get(token, 0) + 1
    return feature

def convert_to_dict(data):
    result = []
    for _, row in data.iterrows():
        text = row['sentence']
        label = row['label']
        feature = text_to_feature(text)
        result.append({'text': text, 'label': label, 'feature': feature})
    return result

train_data = convert_to_dict(train)
dev_data = convert_to_dict(dev)

# 正則化パラメータの範囲
C_values = [0.01, 0.1, 1, 10, 100]

# 正解率を格納するリスト
accuracies = []

# 特徴量のベクトル化
vectorizer = DictVectorizer(sparse=False)
X_train = vectorizer.fit_transform([data['feature'] for data in train_data])
X_dev = vectorizer.transform([data['feature'] for data in dev_data])

# ラベルの抽出
y_train = [data['label'] for data in train_data]
y_dev = [data['label'] for data in dev_data]

# 正則化パラメータを変化させながらモデルを学習
for C in C_values:
    model = LogisticRegression(C=C, max_iter=1000)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_dev)
    accuracy = accuracy_score(y_dev, y_pred)
    accuracies.append(accuracy)
    print(f"C={C}, Accuracy={accuracy:.4f}")

# グラフの描画
plt.figure(figsize=(8, 6))
plt.plot(C_values, accuracies, marker='o')
plt.xscale('log')  # 正則化パラメータを対数スケールで表示
plt.xlabel('Regularization Parameter (C)')
plt.ylabel('Accuracy')
plt.title('Effect of Regularization Parameter on Accuracy')
plt.grid(True)
plt.show()