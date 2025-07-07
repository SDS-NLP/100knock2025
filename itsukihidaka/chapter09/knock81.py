# “The movie was full of [MASK].”の”[MASK]”を埋めるのに最も適切なトークンを求めよ。
from transformers import pipeline

# マスク予測用パイプラインを準備
unmasker = pipeline("fill-mask", model="bert-base-uncased")

# 入力文（[MASK]がトークンのまま）
sentence = "The movie was full of [MASK]."

# マスク予測の実行
results = unmasker(sentence, top_k=1)

# 結果を表示
print(results)
