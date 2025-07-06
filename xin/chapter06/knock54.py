import gensim.downloader as api
from numpy.linalg import norm
import numpy as np
import urllib.request

# モデル読み込み
model = api.load("glove-wiki-gigaword-100")

# データのダウンロード（Googleのアナロジーデータ）
url = "https://raw.githubusercontent.com/RaRe-Technologies/gensim/develop/gensim/test/test_data/questions-words.txt"
local_path = "questions-words.txt"
urllib.request.urlretrieve(url, local_path)

# アナロジー評価（capital-common-countries セクションのみ）
results = []
with open(local_path, encoding="utf-8") as f:
    use_section = False
    for line in f:
        if line.startswith(":"):
            use_section = line.strip() == ": capital-common-countries"
            continue
        if not use_section:
            continue
        w1, w2, w3, actual = line.strip().lower().split()

        # 単語がすべて語彙にあるか確認
        if all(word in model for word in (w1, w2, w3)):
            vec = model[w2] - model[w1] + model[w3]
            # 語彙の中から最も近い単語を1つ取得（topn=1）
            predicted, similarity = model.similar_by_vector(vec, topn=1)[0]
            is_correct=predicted==actual
            results.append((w1, w2, w3, actual, predicted, similarity, is_correct))
            total+=1
            if is_correct:
                correct += 1

# 結果表示（上位10件のみ）
print("w1\tw2\tw3\tactual\tpredicted\tsimilarity")
for r in results[:10]:
    print("\t".join(r[:4]), f"{r[4]}\t{r[5]:.4f}")
