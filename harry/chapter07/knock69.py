# 69. 正則化パラメータの変更
# ロジスティック回帰モデルを学習するとき、正則化の係数（ハイパーパラメータ）を調整することで、
# 学習時の適合度合いを制御できる。正則化の係数を変化させながらロジスティック回帰モデルを学習し、
# 検証データ上の正解率を求めよ。実験の結果は、正則化パラメータを横軸、正解率を縦軸としたグラフにまとめよ。

# ファイル名: knock69.py
# 目的: 正則化パラメータ C を変えて検証データでの正解率を評価・可視化

import os
import pickle
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction import DictVectorizer

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def extract_X_y(data):
    X = [ex['feature'] for ex in data]
    y = [int(ex['label']) for ex in data]
    return X, y

def main():
    # フォント設定（Noto Sans CJK JP を直接使う）
    font_path = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
    if os.path.exists(font_path):
        font_prop = fm.FontProperties(fname=font_path)
        print(f"✅ フォント設定（font_prop）に読み込み成功: {font_prop.get_name()}")
    else:
        print("⚠️ フォントファイルが見つかりません。日本語が表示されない可能性があります。")

    # === 📁 パス設定 ===
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')
    train_data = load_pickle(os.path.join(output_dir, 'train_bow.pkl'))
    dev_data = load_pickle(os.path.join(output_dir, 'dev_bow.pkl'))

    # === 特徴ベクトル化 ===
    X_train_dicts, y_train = extract_X_y(train_data)
    X_dev_dicts, y_dev = extract_X_y(dev_data)

    vectorizer = DictVectorizer(sparse=True)
    X_train = vectorizer.fit_transform(X_train_dicts)
    X_dev = vectorizer.transform(X_dev_dicts)

    # === C 値のリスト ===
    C_list = [0.01, 0.1, 1, 10, 100]
    accuracy_list = []

    print("🔍 各Cにおける検証精度:")
    for C in C_list:
        model = LogisticRegression(C=C, max_iter=1000)
        model.fit(X_train, y_train)
        y_pred = model.predict(X_dev)
        acc = accuracy_score(y_dev, y_pred)
        accuracy_list.append(acc)
        print(f"C={C:<6} -> Accuracy={acc:.4f}")

    # グラフ描画
    plt.figure()
    plt.plot(C_list, accuracy_list, marker='o')
    plt.xscale('log')
    plt.xlabel("正則化パラメータ C（対数スケール）", fontproperties=font_prop)
    plt.ylabel("検証データの正解率", fontproperties=font_prop)
    plt.title("Cと正解率の関係", fontproperties=font_prop)

    # === 📁 グラフ保存と表示 ===
    result_path = os.path.join(output_dir, "knock69_result.png")
    plt.savefig(result_path)
    plt.show()
    print(f"📊 グラフを保存しました: {result_path}")

if __name__ == '__main__':
    main()
