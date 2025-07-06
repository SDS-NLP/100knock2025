#!/usr/bin/env python
# coding: utf-8

# In[4]:


import csv
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

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

vectorizer = DictVectorizer(sparse=True)
X_train = vectorizer.fit_transform(train_features) 

model = LogisticRegression(max_iter=1000)
model.fit(X_train, train_labels)

print("--- モデル学習完了 ---")

def evaluate_model(X, y_true, model, dataset_name):
    y_pred = model.predict(X)

    accuracy = accuracy_score(y_true, y_pred)

    precision = precision_score(y_true, y_pred, pos_label=1)
    recall = recall_score(y_true, y_pred, pos_label=1)
    f1 = f1_score(y_true, y_pred, pos_label=1)

    print(f"\n--- {dataset_name}での評価指標 ---")
    print(f"正解率: {accuracy:.4f}")
    print(f"適合率: {precision:.4f}")
    print(f"再現率: {recall:.4f}")
    print(f"F1スコア: {f1:.4f}")

    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    print("\n混同行列:")
    print(cm)

evaluate_model(X_train, train_labels, model, "訓練データ")

dev_features = [d['feature'] for d in dev_data]
dev_labels = [int(d['label']) for d in dev_data]
X_dev = vectorizer.transform(dev_features)

evaluate_model(X_dev, dev_labels, model, "検証データ")

