from transformers import pipeline

# マスク予測用パイプラインを準備（bert-base-uncased）
unmasker = pipeline("fill-mask", model="bert-base-uncased", top_k=10)

# 入力文（[MASK] を明示的に指定）
text = "The movie was full of [MASK]."

# 予測
results = unmasker(text)

# 出力
print("Top-10予測:")
for r in results:
    token = r["token_str"]
    prob = r["score"]
    print(f"{token:15s}  尤度: {prob:.4f}")
