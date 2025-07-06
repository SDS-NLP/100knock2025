import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from knock63 import train_labels, train_dicts, dev_dicts, dev_labels

# CountVectorizerのインスタンス作成（テキスト前処理は必要に応じて調整）
vectorizer = DictVectorizer()

# テキストデータをBoWに変換
X_train = vectorizer.fit_transform(train_dicts)
X_dev = vectorizer.transform(dev_dicts)

# ロジスティック回帰モデルの学習
clf = LogisticRegression(max_iter=1000)
clf.fit(X_train, train_labels)

# 特徴語と重みを取得
feature_names = vectorizer.get_feature_names_out()
weights = clf.coef_[0]

# 特徴語とその重みのペアを作成し、重みでソート
feature_weights = list(zip(feature_names, weights))
sorted_weights = sorted(feature_weights, key=lambda x: x[1], reverse=True)

# 上位20個（ポジティブに寄与）
top20 = sorted_weights[:20]

# 下位20個（ネガティブに寄与）
bottom20 = sorted_weights[-20:]

# 結果出力
print("Top 20 Positive Features (推定ラベル=1に寄与):")
for word, weight in top20:
    print(f"{word:>15} : {weight:.4f}")

print("\nTop 20 Negative Features (推定ラベル=0に寄与):")
for word, weight in bottom20:
    print(f"{word:>15} : {weight:.4f}")
