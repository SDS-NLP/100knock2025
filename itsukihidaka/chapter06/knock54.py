# 単語アナロジーの評価データをダウンロードし、国と首都に関する事例（: capital-common-countriesセクション）に対して、vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し、そのベクトルと類似度が最も高い単語と、その類似度を求めよ。求めた単語と類似度は、各事例と一緒に記録せよ。

from gensim.models import KeyedVectors
import pandas as pd

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True)

with open('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter06/questions-words.txt', 'r') as f:
    lines = []
    start_collecting = False
    
    for line in f:
        if line.startswith(': capital-common-countries'):
            start_collecting = True
            continue
        elif line.startswith(':') and start_collecting:
            break
        elif start_collecting:
            words = line.strip().split()
            lines.append(words)
    
    df = pd.DataFrame(lines, columns=['word1', 'word2', 'word3', 'word4'])

    # 結果を格納するリスト
    similar_words = []
    similar_vectors = []
    similarities = []

    # 各行に対して計算を実行
    for _, row in df.iterrows():
        # 最も類似度の高い単語を取得
        most_similar = model.most_similar(positive=[row['word2'], row['word3']], negative=[row['word1']], topn=1)[0]
        
        # 結果をリストに追加
        similar_words.append(most_similar[0])
        similar_vectors.append(model[row['word2']] - model[row['word1']] + model[row['word3']])
        similarities.append(most_similar[1])

    # 結果をDataFrameに追加
    df['similar_word'] = similar_words
    df['similar_vector'] = similar_vectors
    df['similarity'] = similarities

    print(df)

    df.to_csv('/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter06/knock54.csv', index=False)            
