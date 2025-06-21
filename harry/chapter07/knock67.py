# 67. 精度の計測
# 学習したロジスティック回帰モデルの正解率、適合率、再現率、F1スコアを、学習データおよび検証データ上で計測せよ。

# ファイル名: knock67.py
# 目的: 学習データと検証データの正解率・適合率・再現率・F1スコアを計測する

import os
import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def extract_X_y(data):
    X = [ex['feature'] for ex in data]
    y = [int(ex['label']) for ex in data]
    return X, y

def evaluate(model, vectorizer, data, name="データ"):
    X_dict, y_true = extract_X_y(data)
    X = vectorizer.transform(X_dict)
    y_pred = model.predict(X)

    acc = accuracy_score(y_true, y_pred)
    pre = precision_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred)
    f1  = f1_score(y_true, y_pred)

    print(f"\n📊 {name} における評価指標")
    print(f"正解率 (Accuracy):     {acc:.4f}")
    print(f"適合率 (Precision):    {pre:.4f}")
    print(f"再現率 (Recall):       {rec:.4f}")
    print(f"F1スコア (F1 score):   {f1:.4f}")

def main():
    # パス設定
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')
    model = load_pickle(os.path.join(output_dir, 'logreg_model.pkl'))
    vectorizer = load_pickle(os.path.join(output_dir, 'vectorizer.pkl'))
    train_data = load_pickle(os.path.join(output_dir, 'train_bow.pkl'))
    dev_data = load_pickle(os.path.join(output_dir, 'dev_bow.pkl'))

    # 学習データと検証データで評価
    evaluate(model, vectorizer, train_data, name="学習データ")
    evaluate(model, vectorizer, dev_data, name="検証データ")

if __name__ == '__main__':
    main()
