#64. 条件付き確率
from knock61 import dev_data
from knock62 import clf, vectorizer, label_encoder

# 検証データの先頭の事例
example = dev_data[0]
true_label = example['label']
feature_dict = example['feature']

# 特徴ベクトルに変換（DictVectorizerで整形）
X_example = vectorizer.transform([feature_dict])

# ラベル予測
#pred_label_num = clf.predict(X_example)[0]                # 数値ラベル（例: 0 or 1）
#pred_label = label_encoder.inverse_transform([pred_label_num])[0]  # 元のラベルに変換（例: '0' or '1'）
probs = clf.predict_proba(X_example)[0]

# 結果表示
print("検証データの先頭の事例:")
print("テキスト:", example['text'])
#print("正解ラベル:", true_label)
#print("予測ラベル:", pred_label)
print("条件付き確率：", "ネガティブ(0)", f"{probs[0]:.4f}","ポジティブ(1)", f"{probs[1]:.4f}")

# 一致確認
#if pred_label == true_label:
#    print("一致")
#else:
#    print("不一致")
