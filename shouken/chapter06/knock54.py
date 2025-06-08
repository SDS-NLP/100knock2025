from gensim.models import KeyedVectors

# 1. モデル読み込み
model_path = "GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 2. アナロジーデータ読み込み
analogy_path = "questions-words.txt"
results = []

with open(analogy_path, encoding="utf-8") as f:
    section = None
    for line in f:
        line = line.strip()
        if line.startswith(":"):
            section = line[2:]  # 例: "capital-common-countries"
            continue
        if section != "capital-common-countries":
            continue

        w1, w2, w3, _ = line.lower().split()
        try:
            # 3. アナロジーベクトル計算
            predicted = model.most_similar(positive=[w2, w3], negative=[w1], topn=1)[0]
            predicted_word, similarity = predicted
            results.append((w1, w2, w3, predicted_word, similarity))
        except KeyError:
            # モデルに含まれていない単語がある場合はスキップ
            results.append((w1, w2, w3, None, None))

# 4. 結果を表示
for w1, w2, w3, pred, sim in results:
    print(f"{w1} {w2} {w3} -> {pred} (similarity={sim:.4f})" if pred else f"{w1} {w2} {w3} -> [OOV]")
