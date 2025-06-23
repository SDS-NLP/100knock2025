#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

base_path = "/Users/niaomuqing/100knock2025/SST-2/"

train_df = pd.read_csv(base_path + "train.tsv", sep='\t')
dev_df = pd.read_csv(base_path + "dev.tsv", sep='\t')

train_counts = train_df['label'].value_counts().sort_index()
dev_counts = dev_df['label'].value_counts().sort_index()

print("SST-2: Train Data")
print(f"Negative (0): {train_counts.get(0, 0)}")
print(f"Positive (1): {train_counts.get(1, 0)}")

print("\nSST-2: Dev Data")
print(f"Negative (0): {dev_counts.get(0, 0)}")
print(f"Positive (1): {dev_counts.get(1, 0)}")

