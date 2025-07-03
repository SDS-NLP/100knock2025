#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression

base_path = "/Users/niaomuqing/100knock2025/SST-2/"
train_path = base_path + "train.tsv"
dev_path = base_path + "dev.tsv"

def load_and_transform_tsv(path):
    data_list = []
    with open(path, encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            text = row['sentence']
            label = row['label']
            tokens = text.split()
            feature = dict(Counter(tokens))
            data_list.append({
                'text': text,
                'label': label,
                'feature': feature
            })
    return data_list

train_data = load_and_transform_tsv(train_path)

train_features = [d['feature'] for d in train_data]
train_labels = [int(d['label']) for d in train_data]
vectorizer = DictVectorizer(sparse=True)
X_train = vectorizer.fit_transform(train_features)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, train_labels)

print("--- モデル学習完了 ---")

feature_names = vectorizer.get_feature_names_out()

coefficients = model.coef_[0]

feature_weights = list(zip(coefficients, feature_names))

feature_weights_sorted = sorted(feature_weights, key=lambda x: x[0], reverse=True)

print("\n--- 重みの高い特徴量トップ20 (Top 20 High-Weight Features) ---")

for i, (weight, feature) in enumerate(feature_weights_sorted[:20]):
    print(f"{i+1}. {feature}: {weight:.4f}")

print("\n--- 重みの低い特徴量トップ20 (Top 20 Low-Weight Features) ---")

for i, (weight, feature) in enumerate(feature_weights_sorted[-20:]):
    print(f"{i+1}. {feature}: {weight:.4f}")

