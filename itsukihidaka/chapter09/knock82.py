# "The movie was full of [MASK]."の"[MASK]"に埋めるのに適切なトークン上位10個と、その確率（尤度）を求めよ。

from transformers import pipeline

# マスク予測用パイプラインを準備
unmasker = pipeline("fill-mask", model="bert-base-uncased")

# 入力文（[MASK]がトークンのまま）
sentence = "The movie was full of [MASK]."

# マスク予測の実行（上位10候補を取得）
results = unmasker(sentence, top_k=10)

# 結果を表示（上位10候補）
print("上位10個のトークンとその確率（尤度）:")
print("-" * 50)
for i, result in enumerate(results, 1):
    print(f"{i:2d}. {result['sequence']} -> 確率: {result['score']:.4f}")