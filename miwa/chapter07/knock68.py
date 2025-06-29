#68. 特徴量の重みの確認
from knock62 import clf, vectorizer

# 特徴名（単語リスト）
feature_names = vectorizer.get_feature_names_out()

# ロジスティック回帰の係数（クラス1に対する重み）
coef = clf.coef_[0]  # 1次元配列（各特徴に対する重み）

# 特徴と係数を対応づける
feature_weights = list(zip(feature_names, coef))

# 正の重み（ポジティブ寄り）でソート
top_positive = sorted(feature_weights, key=lambda x: x[1], reverse=True)[:20]

# 負の重み（ネガティブ寄り）でソート
top_negative = sorted(feature_weights, key=lambda x: x[1])[:20]

# 結果表示
print("ポジティブ寄りの特徴トップ20:")
for word, weight in top_positive:
    print(f"{word:20s}: {weight:.4f}")

print("ネガティブ寄りの特徴トップ20:")
for word, weight in top_negative:
    print(f"{word:20s}: {weight:.4f}")
