import joblib
from knock61 import dev_examples
# confusion_matrix : 真値と予測値を集計して 2 × 2 の混同行列を返す関数
from sklearn.metrics import confusion_matrix


# ロジスティック回帰モデルとベクトライザを読み込み
model, vectorizer = joblib.load("logistic_model.joblib")

# 特徴量とラベルを抽出
X_dev_dict = [ex["feature"] for ex in dev_examples]
y_true = [int(ex["label"]) for ex in dev_examples] 

# Bag-of-Words 形式の辞書を数値ベクトルに変換
X_dev = vectorizer.transform(X_dev_dict)

# 予測（予測ラベルは0または1）
y_pred = model.predict(X_dev)

# 混同行列の作成
cm = confusion_matrix(y_true, y_pred)

print("混同行列：")
print(cm)

#出力
"""混同行列：
[[335  93]
 [ 73 371]]"""

 
"""
[[TN FP]
[FN TP]]"""
