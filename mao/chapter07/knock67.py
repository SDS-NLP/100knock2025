"""
knock67:精度の計測
学習したロジスティック回帰モデルの正解率、適合率、再現率、F1スコアを、
学習データおよび検証データ上で計測せよ。
"""
from knock62 import model, vectorizer, train_features, train_labels
from knock61 import dev_bow
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

#学習データ
X_train = vectorizer.transform(train_features)
y_train = [int(label) for label in train_labels]
y_train_pred = model.predict(X_train)

#検証データ
X_dev = vectorizer.transform([entry['feature'] for entry in dev_bow])
y_dev = [int(entry['label']) for entry in dev_bow]
y_dev_pred = model.predict(X_dev)

# === 指標計算関数 ===
def evaluate(y_true, y_pred, dataset_name):
    print(f"--- {dataset_name} ---")
    print("Accuracy :", accuracy_score(y_true, y_pred))
    print("Precision:", precision_score(y_true, y_pred))
    print("Recall   :", recall_score(y_true, y_pred))
    print("F1 Score :", f1_score(y_true, y_pred))
    print()

# 結果出力
evaluate(y_train, y_train_pred, "Train")
evaluate(y_dev, y_dev_pred, "Dev")
