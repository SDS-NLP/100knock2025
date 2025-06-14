# 64. 条件付き確率
# 学習したロジスティック回帰モデルを用い、検証データの先頭の事例を各ラベル（ポジネガ）に分類するときの条件付き確率を求めよ。

# ファイル名: predict_proba_one.py
# 目的: 検証データの先頭1件に対して、各ラベルの条件付き確率を表示する

import os
import pickle

def load_pickle(filepath):
    with open(filepath, 'rb') as f:
        return pickle.load(f)

def main():
    # パス設定
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')

    # モデル、ベクトライザー、検証データを読み込み
    model = load_pickle(os.path.join(output_dir, 'logreg_model.pkl'))
    vectorizer = load_pickle(os.path.join(output_dir, 'vectorizer.pkl'))
    dev_data = load_pickle(os.path.join(output_dir, 'dev_bow.pkl'))

    # 検証データの先頭1件
    example = dev_data[0]
    text = example['text']
    true_label = int(example['label'])
    feature_dict = example['feature']

    # ベクトル化
    X = vectorizer.transform([feature_dict])

    # 条件付き確率を計算
    probas = model.predict_proba(X)[0]  # [0] で 1次元配列に変換

    # クラスの並びを確認
    classes = model.classes_  # 例: array([0, 1])

    # 出力
    print("📝 テキスト:")
    print(text)
    print("\n📊 条件付き確率:")
    for label, proba in zip(classes, probas):
        polarity = "ネガティブ" if label == 0 else "ポジティブ"
        print(f" P(ラベル={label}｜この文) = {proba:.4f}　← {polarity}")
    print(f"\n✅ 正解ラベル: {true_label}")

if __name__ == '__main__':
    main()
