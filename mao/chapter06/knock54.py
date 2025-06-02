"""
knock54:アナロジーデータでの実験
単語アナロジーの評価データをダウンロードし、国と首都に関する事例（: capital-common-countriesセクション）
に対して、vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し、
そのベクトルと類似度が最も高い単語と、その類似度を求めよ。
求めた単語と類似度は、各事例と一緒に記録せよ
"""
from gensim.models import KeyedVectors

#モデル,データ読み込み
questions_path="mao/chapter06/questions-words.txt"
model_path="mao/chapter06/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 出力結果の保存リスト
results = []

with open(questions_path, encoding="utf-8") as f:
    section = None
    for line in f:
        line = line.strip()

        #セクションタイトル
        if line.startswith(":"):
            section = line[2:]
            continue

        #:capital-common-countries 以外はスキップ
        if section != "capital-common-countries":
            continue

        #単語A, B, C, D（Dは正解）
        A, B, C, D = line.split()

        #単語が語彙にあるかチェック
        if all(w in model for w in [A, B, C]):
            try:
                # アナロジー計算
                predicted=model.most_similar(positive=[B, C], negative=[A], topn=1)[0]
                predicted_word, similarity=predicted
            except KeyError:
                predicted_word, similarity="N/A",0.0
        else:
            predicted_word, similarity="N/A",0.0

        #結果保存
        results.append((A, B, C, D, predicted_word, similarity))

#結果確認
for row in results[:5]:
    print("\t".join(map(str, row)))
