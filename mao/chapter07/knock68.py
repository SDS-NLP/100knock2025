"""
knock68:特徴量の重みの確認
学習したロジスティック回帰モデルの中で、重みの高い特徴量トップ20と、
重みの低い特徴量トップ20を確認せよ。
"""
from knock62 import model, vectorizer

# 特徴語（単語）の一覧を取得
feature_names = vectorizer.get_feature_names_out()

# 重みベクトルを取得（logistic回帰では coef_ は shape = (1, n_features)）
weights = model.coef_[0]

# 重みと単語をペアにする
feature_weights = list(zip(feature_names, weights))

# 重みでソート
sorted_by_weight = sorted(feature_weights, key=lambda x: x[1], reverse=True)

# 上位・下位20件を抽出
top_positive = sorted_by_weight[:20]
top_negative = sorted_by_weight[-20:]

# 出力
print("★ Positive（重みが大きい）特徴量 Top 20")
for word, weight in top_positive:
    print(f"{word:<15}: {weight:.4f}")

print("\n★ Negative（重みが小さい）特徴量 Top 20")
for word, weight in top_negative:
    print(f"{word:<15}: {weight:.4f}")
