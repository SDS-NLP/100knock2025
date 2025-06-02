# “Spain”の単語ベクトルから”Madrid”のベクトルを引き、”Athens”のベクトルを足したベクトルを計算し、そのベクトルと類似度の高い10語とその類似度を出力せよ。

from gensim.models import KeyedVectors

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True)

Spain_vector = model['Spain']
Madrid_vector = model['Madrid']
Athens_vector = model['Athens']

result_vector = Spain_vector - Madrid_vector + Athens_vector

for word, similarity in model.most_similar(result_vector, topn=10):
    print(f'{word}: {similarity}')