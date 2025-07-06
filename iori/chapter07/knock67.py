import pandas as pd
from knock62 import model, vectorizer
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import re
from collections import Counter

train = pd.read_csv('SST-2/train.tsv', sep='\t')
dev = pd.read_csv('SST-2/dev.tsv', sep='\t')
# 特徴量の辞書化
def text_to_feature(text):
    tokens = re.findall(r'\w+|[^\w\s]', text)
    return dict(Counter(tokens))

train_predictions = model.predict(vectorizer.transform([text_to_feature(text) for text in train['sentence']]))
train_accuracy = accuracy_score(train['label'], train_predictions)
train_precision = precision_score(train['label'], train_predictions)
train_recall = recall_score(train['label'], train_predictions)
train_f1 = f1_score(train['label'], train_predictions)

print("Training Data Metrics:")
print(f"Accuracy: {train_accuracy:.4f}")
print(f"Precision: {train_precision:.4f}")
print(f"Recall: {train_recall:.4f}")
print(f"F1 Score: {train_f1:.4f}")

dev_predictions = model.predict(vectorizer.transform([text_to_feature(text) for text in dev['sentence']]))
dev_accuracy = accuracy_score(dev['label'], dev_predictions)
dev_precision = precision_score(dev['label'], dev_predictions)
dev_recall = recall_score(dev['label'], dev_predictions)
dev_f1 = f1_score(dev['label'], dev_predictions)

print("\ndev Data Metrics:")
print(f"Accuracy: {dev_accuracy:.4f}")
print(f"Precision: {dev_precision:.4f}")
print(f"Recall: {dev_recall:.4f}")
print(f"F1 Score: {dev_f1:.4f}")