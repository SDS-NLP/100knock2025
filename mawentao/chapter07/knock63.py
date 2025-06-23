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
dev_data = load_and_transform_tsv(dev_path)

train_features = [d['feature'] for d in train_data]
train_labels = [int(d['label']) for d in train_data]

vectorizer = DictVectorizer(sparse=True)
X_train = vectorizer.fit_transform(train_features)

model = LogisticRegression(max_iter=1000)
model.fit(X_train, train_labels)

print("モデル学習完了")

dev_instance = dev_data[0]
X_dev = vectorizer.transform([dev_instance['feature']])
predicted_label = model.predict(X_dev)[0]
true_label = int(dev_instance['label'])

print("文:", dev_instance['text'])
print("正解ラベル:", true_label)
print("予測ラベル:", predicted_label)
print("一致？", "はい！正解です！" if predicted_label == true_label else "いいえ。間違いです。")

