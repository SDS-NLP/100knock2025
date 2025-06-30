#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import numpy as np

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
dev_data = load_and_transform_tsv(dev_path)

train_features = [d['feature'] for d in train_data]
train_labels = [int(d['label']) for d in train_data]

dev_features = [d['feature'] for d in dev_data]
dev_labels = [int(d['label']) for d in dev_data]

vectorizer = DictVectorizer(sparse=True)
X_train = vectorizer.fit_transform(train_features)
X_dev = vectorizer.transform(dev_features)

print("--- データ準備完了 ---")

C_values = np.logspace(-3, 3, 7)


accuracies = [] 

print("\n--- 正則化パラメータ (C) の変化と正解率の計測 ---")

for c in C_values:
    print(f"\nトレーニングモデル with C = {c:.6f}...")

    model = LogisticRegression(C=c, max_iter=1000, solver='liblinear') 
    model.fit(X_train, train_labels)

    dev_predictions = model.predict(X_dev)

    accuracy = accuracy_score(dev_labels, dev_predictions)
    accuracies.append(accuracy)

    print(f"  検証データでの正解率 (Accuracy) = {accuracy:.4f}")

print("\n--- 全てのC値での評価完了 ---")

plt.figure(figsize=(10, 6))
plt.plot(C_values, accuracies, marker='o', linestyle='-')
plt.xscale('log')
plt.xlabel("正則化パラメータ C (Regularization Parameter C)")
plt.ylabel("検証データ正解率 (Validation Data Accuracy)")
plt.title("正則化パラメータ C と正解率の関係 (C vs. Accuracy)")
plt.grid(True) 
plt.xticks(C_values, [f'{c:.3f}' for c in C_values])
plt.tight_layout() 
plt.show() 

