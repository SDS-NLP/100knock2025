# 学習したロジスティック回帰モデルの中で、重みの高い特徴量トップ20と、重みの低い特徴量トップ20を確認せよ。
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

# データセットの読み込み
df_train = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/train.tsv', sep='\t')
df_dev = pd.read_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter07/SST-2/dev.tsv', sep='\t')

# ラベルの準備
texts = df_train['sentence'].tolist()
labels = df_train['label'].tolist()

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# ロジスティック回帰モデルの学習
model = LogisticRegression(random_state=42)
model.fit(X, labels)

# 特徴量名（単語）と重みを取得
feature_names = vectorizer.get_feature_names_out()
weights = model.coef_[0]

# 重みと特徴量名を組み合わせてDataFrameを作成
weight_df = pd.DataFrame({
    'feature': feature_names,
    'weight': weights
})

# 重みの高い特徴量トップ20（正の値）
print("重みの高い特徴量トップ20（ポジティブな影響）:")
top_positive = weight_df.nlargest(20, 'weight')
for i, (_, row) in enumerate(top_positive.iterrows(), 1):
    print(f"{i:2d}. {row['feature']:15s}: {row['weight']:8.4f}")

print("\n" + "="*50 + "\n")

# 重みの低い特徴量トップ20（負の値）
print("重みの低い特徴量トップ20（ネガティブな影響）:")
top_negative = weight_df.nsmallest(20, 'weight')
for i, (_, row) in enumerate(top_negative.iterrows(), 1):
    print(f"{i:2d}. {row['feature']:15s}: {row['weight']:8.4f}")






