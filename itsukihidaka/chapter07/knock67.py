import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')
df_dev = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/dev.tsv', sep='\t')

# ラベルの準備
texts = df_train['sentence'].tolist()
labels = df_train['label'].tolist()

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# ロジスティック回帰モデルの学習
model = LogisticRegression(random_state=42)
model.fit(X, labels)

# テストデータで精度検証
texts_dev = df_dev['sentence'].tolist()
labels_dev = df_dev['label'].tolist()
X_dev = vectorizer.transform(texts_dev)

# テストデータでの予測
predictions = model.predict(X_dev)

# TN, FP, FN, TP
TN = np.sum((predictions == 0) & (np.array(labels_dev) == 0))
FP = np.sum((predictions == 1) & (np.array(labels_dev) == 0))
FN = np.sum((predictions == 0) & (np.array(labels_dev) == 1))
TP = np.sum((predictions == 1) & (np.array(labels_dev) == 1))
print(f"TN: {TN}, FP: {FP}, FN: {FN}, TP: {TP}")

# 検証データ
print('---検証データ---')
# 正解率
print("正解率:")
print((predictions == labels_dev).mean())

# 適合率
print("適合率:")
print(TP / (TP + FP))

# 再現率
print("再現率:")
print(TP / (TP + FN))

# F1スコア
print("F1スコア:")
print(2 * TP / (2 * TP + FP + FN))

# 学習データ
print('---学習データ---')
train_predictions = model.predict(X)

# TN, FP, FN, TP
TN = np.sum((train_predictions == 0) & (np.array(labels) == 0))
FP = np.sum((train_predictions == 1) & (np.array(labels) == 0))
FN = np.sum((train_predictions == 0) & (np.array(labels) == 1))
TP = np.sum((train_predictions == 1) & (np.array(labels) == 1))
print(f"TN: {TN}, FP: {FP}, FN: {FN}, TP: {TP}")

# 正解率
print("正解率:")
print((train_predictions == labels).mean())

# 適合率
print("適合率:")
print(TP / (TP + FP))

# 再現率
print("再現率:")
print(TP / (TP + FN))

# F1スコア
print("F1スコア:")
print(2 * TP / (2 * TP + FP + FN))