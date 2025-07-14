#評価する関数を作成

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(X_dict, y_true, model, vectorizer, name=""):
    # ベクトル化
    X_vec = vectorizer.transform(X_dict)
    
    # 予測
    y_pred = model.predict(X_vec)
    
    # スコア計算
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print(f"{name}データの評価：")
    print(f"正解率 : {acc:.4f}")
    print(f"適合率 : {prec:.4f}")
    print(f"再現率 : {rec:.4f}")
    print(f"F1スコア : {f1:.4f}")
    print()

#学習データと検証データで計測する

import joblib
from knock61 import train_examples, dev_examples

# モデルとベクトライザを読み込み
model, vectorizer = joblib.load("logistic_model.joblib")

# 学習データ
X_train_dict = [ex["feature"] for ex in train_examples]
y_train = [int(ex["label"]) for ex in train_examples]

# 検証データ
X_dev_dict = [ex["feature"] for ex in dev_examples]
y_dev = [int(ex["label"]) for ex in dev_examples]

# 評価
evaluate_model(X_train_dict, y_train, model, vectorizer, name="学習")
evaluate_model(X_dev_dict, y_dev, model, vectorizer, name="検証")

#出力
"""学習データの評価：
正解率 : 0.9421
適合率 : 0.9427
再現率 : 0.9542
F1スコア : 0.9484

検証データの評価：
正解率 : 0.8096
適合率 : 0.7996
再現率 : 0.8356
F1スコア : 0.8172"""