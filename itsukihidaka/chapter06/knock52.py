# “United States”とコサイン類似度が高い10語と、その類似度を出力せよ。

from gensim.models import KeyedVectors

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True)

for word, similarity in model.most_similar('United_States', topn=10):
    print(f'{word}: {similarity}')


