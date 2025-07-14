from knock62 import model  # Pipeline（DictVectorizer + LogisticRegression）
from collections import Counter

# 入力テキスト
text = "the worst movie I 've ever seen"

# 単語の出現頻度をBoWとして構築（knock61と同じ方法）
tokens = text.split()
feature = dict(Counter(tokens))

# ラベル予測と確率
predicted_label = model.predict([feature])[0]
prob = model.predict_proba([feature])[0]

# 結果表示
print(f"テキスト: {text}")
print(f"予測ラベル: {predicted_label} ({'ポジティブ' if predicted_label == 1 else 'ネガティブ'})")
print(f"確率: ラベル0（ネガティブ）={prob[0]:.4f}, ラベル1（ポジティブ）={prob[1]:.4f}")
