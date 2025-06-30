"""
knock65:テキストのポジネガの予測
与えられたテキストのポジネガを予測するプログラムを実装せよ。
例えば、テキストとして”the worst movie I ‘ve ever seen”を与え、
ロジスティック回帰モデルの予測結果を確認せよ。
"""
from knock62 import model, vectorizer
from collections import Counter

# 生テキストをBoW辞書に変換
def text_to_bow(text):
    tokens = text.split()
    return dict(Counter(tokens))

# ポジネガ予測関数
def predict_label(text):
    # 1. テキストをBoW辞書に変換
    feature_dict = text_to_bow(text)
    # 2. ベクトル化
    X_input = vectorizer.transform([feature_dict])
    # 3. 予測
    predicted_label = model.predict(X_input)[0]
    return predicted_label

# テスト用テキスト
text = "the worst movie I've ever seen"

print("テキスト :", text)
print("予測ラベル:", predict_label(text))
