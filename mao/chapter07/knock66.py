"""
knock66:混同行列の作成
学習したロジスティック回帰モデルの検証データにおける
混同行列（confusion matrix）を求めよ。
"""
from knock62 import model, vectorizer
from knock61 import dev_bow
from sklearn.metrics import confusion_matrix

# 1. 特徴ベクトルと正解ラベルを抽出
features = [entry['feature'] for entry in dev_bow]
true_labels = [int(entry['label']) for entry in dev_bow]

# 2. 特徴ベクトルをベクトル化
X_dev = vectorizer.transform(features)

# 3. 予測ラベルを取得
predicted_labels = model.predict(X_dev)

# 4. 混同行列を算出
cm = confusion_matrix(true_labels, predicted_labels)

# 5. 表示
print("混同行列:\n", cm)
