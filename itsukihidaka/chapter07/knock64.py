import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

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

# 先頭の事例について条件付き確率を計算
probabilities = model.predict_proba(X_dev[0])
print(f"先頭の事例の文: {texts_dev[0]}")
print(f"ネガティブ(0)の確率: {probabilities[0][0]:.3f}")
print(f"ポジティブ(1)の確率: {probabilities[0][1]:.3f}")



