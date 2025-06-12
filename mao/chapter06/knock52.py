"""
knock52:類似度の高い単語10件
"United States"とコサイン類似度が高い10語と、その類似度を出力せよ
"""
from gensim.models import KeyedVectors

# モデルの読み込み
model_path = "mao/chapter06/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

#target
target="United_States"

#類似度の高い10件を表示
if target in model:
    similar_word=model.most_similar(target,topn=10)
    for word,score in similar_word:
        print(f"{word}：{score:.4f}")
else:
    print(f"'{target}' is not in the vocabulary.")


