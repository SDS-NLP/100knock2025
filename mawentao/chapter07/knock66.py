#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import csv
from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix

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

print("\n--- 開発セットでのモデル評価 (65題の結果) ---")
accuracy = accuracy_score(dev_labels, dev_predictions)
precision = precision_score(dev_labels, dev_predictions, pos_label=1)
recall = recall_score(dev_labels, dev_predictions, pos_label=1)
f1 = f1_score(dev_labels, dev_predictions, pos_label=1)
print(f"Accuracy: {accuracy:.4f}")
print(f"Precision (Positive): {precision:.4f}")
print(f"Recall (Positive): {recall:.4f}")
print(f"F1 Score (Positive): {f1:.4f}")

print("\n--- 開発セットでの混同行列 ---")

cm = confusion_matrix(dev_labels, dev_predictions, labels=[0, 1])

print("混同行列:")
print(cm)

tn, fp, fn, tp = cm.ravel()

print(f"\nTrue Negative (TN): {tn} (实际为0, 预测为0)")
print(f"False Positive (FP): {fp} (实际为0, 预测为1)")
print(f"False Negative (FN): {fn} (实际为1, 预测为0)")
print(f"True Positive (TP): {tp} (实际为1, 预测为1)")

import pandas as pd
cm_df = pd.DataFrame(cm, index=['Actual Negative (0)', 'Actual Positive (1)'],
                     columns=['Predicted Negative (0)', 'Predicted Positive (1)'])
print("\n混同行列 (Pandas DataFrame):")
print(cm_df)


# In[ ]:




