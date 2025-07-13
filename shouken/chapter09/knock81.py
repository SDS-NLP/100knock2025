from transformers import pipeline

# マスク予測用パイプラインの読み込み
unmasker = pipeline("fill-mask", model="bert-base-uncased")

# 入力文（[MASK] はトークンとして正確に指定）
sentence = "The movie was full of [MASK]."

# 予測実行
results = unmasker(sentence)

# 結果表示（上位5件）
for r in results:
    print(f"{r['sequence']} (score={r['score']:.4f})")
