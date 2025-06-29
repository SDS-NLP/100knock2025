#!/usr/bin/env python
# coding: utf-8

# In[2]:


import csv
from collections import Counter

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

print("train_data[0] の中身：")
print(train_data[0])

