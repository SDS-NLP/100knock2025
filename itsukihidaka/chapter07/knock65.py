import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')

# ラベルの準備
texts = df_train['sentence'].tolist()
labels = df_train['label'].tolist()
print(labels)

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# ロジスティック回帰モデルの学習
model = LogisticRegression(random_state=42)
model.fit(X, labels)

# 予測
X_pred = vectorizer.transform(["the worst movie I ‘ve ever seen"])
predictions = model.predict(X_pred)

print(predictions)




