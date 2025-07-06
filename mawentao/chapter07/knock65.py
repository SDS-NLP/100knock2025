#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score 

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

dev_features = [d['feature'] for d in dev_data]
dev_labels = [int(d['label']) for d in dev_data]

X_dev = vectorizer.transform(dev_features)

dev_predictions = model.predict(X_dev)

print("\n--- 開発セットでのモデル評価 ---")

accuracy = accuracy_score(dev_labels, dev_predictions)
print(f"Accuracy: {accuracy:.4f}")

precision = precision_score(dev_labels, dev_predictions, pos_label=1)
print(f"Precision (Positive): {precision:.4f}")

recall = recall_score(dev_labels, dev_predictions, pos_label=1)
print(f"Recall (Positive): {recall:.4f}")

f1 = f1_score(dev_labels, dev_predictions, pos_label=1)
print(f"F1 Score (Positive): {f1:.4f}")

print("\n--- 単一インスタンスの条件付き確率 (from 64題) ---")
dev_instance = dev_data[0] 
X_dev_single = vectorizer.transform([dev_instance['feature']])
probs = model.predict_proba(X_dev_single)[0]

print("文:", dev_instance['text'])
print("条件付き確率:")
print(f"P(label=0 / negative) = {probs[0]:.4f}")
print(f"P(label=1 / positive) = {probs[1]:.4f}")

