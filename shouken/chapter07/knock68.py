from knock62 import model  # Pipeline: DictVectorizer + LogisticRegression

# モデルからベクトル化器と分類器を取得
vectorizer = model.named_steps["vectorizer"]
classifier = model.named_steps["classifier"]

# 特徴量の名前と重み（coef）を取得
feature_names = vectorizer.get_feature_names_out()
weights = classifier.coef_[0]  # 二値分類なので coef_ は shape (1, n_features)

# 特徴語と重みを対応づけてリスト化
features_with_weights = list(zip(feature_names, weights))

# 重み順でソート
sorted_by_weight = sorted(features_with_weights, key=lambda x: x[1], reverse=True)

# 上位・下位20件ずつ表示
print("正の重みトップ20（ポジティブに寄与）")
for word, weight in sorted_by_weight[:20]:
    print(f"{word:20s} {weight:.4f}")

print("\n負の重みトップ20（ネガティブに寄与）")
for word, weight in sorted_by_weight[-20:]:
    print(f"{word:20s} {weight:.4f}")
