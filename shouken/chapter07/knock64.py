from knock61 import dev_data
from knock62 import model  # Pipeline（DictVectorizer + LogisticRegression）

# 検証データの先頭事例
example = dev_data[0]
feature = example['feature']
text = example['text']

# 確率予測
prob = model.predict_proba([feature])[0]  # [0] で1件目の予測結果（[P(0), P(1)]）

# 出力
print(f"テキスト: {text}")
print(f"ラベル0（ネガティブ）である確率: {prob[0]:.4f}")
print(f"ラベル1（ポジティブ）である確率: {prob[1]:.4f}")
