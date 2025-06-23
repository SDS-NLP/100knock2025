import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')

train_list = []
for i in range(len(df_train)):
    train_data = {}
    train_data['text'] = df_train['sentence'][i]
    train_data['label'] = df_train['label'][i]
    BoW = {}
    for word in train_data['text'].split():
        BoW[word] = BoW.get(word, 0) + 1
    train_data['feature'] = BoW
    train_list.append(train_data)

# ラベルの準備
texts = [data['text'] for data in train_list]
labels = [data['label'] for data in train_list]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# ロジスティック回帰モデルの学習
model = LogisticRegression(random_state=42)
model.fit(X, labels)
print(model.coef_)

