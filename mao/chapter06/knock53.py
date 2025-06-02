"""
knock53: 加法構成性によるアナロジー
“Spain”の単語ベクトルから”Madrid”のベクトルを引き、”Athens”のベクトルを足した
ベクトルを計算し、そのベクトルと類似度の高い10語とその類似度を出力せよ。
"""
from gensim.models import KeyedVectors

#モデル読み込み
model_path="mao/chapter06/GoogleNews-vectors-negative300.bin"
model=KeyedVectors.load_word2vec_format(model_path,binary=True)

#アナロジー計算
positive=["Spain","Athens"]
negative=["Madrid"]

for word in positive+negative:
    if word in model:
        results=model.most_similar(positive=positive,negative=negative)
        for word,similarity in results:
            print(f"{word}：{similarity:.4f}")
    else:
        print("One or more words not in vocabulary.")
