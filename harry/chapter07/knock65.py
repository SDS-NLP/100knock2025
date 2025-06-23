# 65. テキストのポジネガの予測
# 与えられたテキストのポジネガを予測するプログラムを実装せよ。
# 例えば、テキストとして”the worst movie I ‘ve ever seen”を与え、
# ロジスティック回帰モデルの予測結果を確認せよ。

# ファイル名: knock65.py
# 目的: コマンドライン引数で与えたテキストに対してポジネガ分類する

import os
import pickle
import sys
from collections import Counter

def load_pickle(path):
    with open(path, 'rb') as f:
        return pickle.load(f)

def text_to_bow(text):
    """
    入力された文字列をBoW特徴ベクトルに変換する
    """
    tokens = text.split()
    return dict(Counter(tokens))

def main():
    # === コマンドライン引数の処理 ===
    if len(sys.argv) < 2:
        print("❌ 使用法: python3 knock65.py '判定したいテキスト'")
        sys.exit(1)

    # 引数を結合して一つの文字列に（スペース含む長文対応）
    text = " ".join(sys.argv[1:])

    # === モデルとベクトライザーを読み込み ===
    base_dir = os.path.dirname(__file__)
    output_dir = os.path.join(base_dir, 'output')
    model = load_pickle(os.path.join(output_dir, 'logreg_model.pkl'))
    vectorizer = load_pickle(os.path.join(output_dir, 'vectorizer.pkl'))

    # BoW変換 → ベクトル化
    bow = text_to_bow(text)
    X = vectorizer.transform([bow])

    # 予測＆確率
    pred = model.predict(X)[0]
    probas = model.predict_proba(X)[0]

    # 結果表示
    print("\n📝 入力テキスト:")
    print(text)
    print("\n📊 条件付き確率:")
    for label, proba in zip(model.classes_, probas):
        polarity = "ネガティブ" if label == 0 else "ポジティブ"
        print(f" P(ラベル={label}｜この文) = {proba:.4f}　← {polarity}")

    print(f"\n🎯 予測ラベル: {pred}（{'ネガティブ' if pred == 0 else 'ポジティブ'}）")

if __name__ == '__main__':
    main()
