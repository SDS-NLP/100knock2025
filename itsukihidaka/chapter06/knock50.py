# Google Newsデータセット（約1,000億単語）での学習済み単語ベクトル（300万単語・フレーズ、300次元）をダウンロードし、"United States"の単語ベクトルを表示せよ。ただし、"United States"は内部的には"United_States"と表現されていることに注意せよ。

from gensim.models import KeyedVectors
import pandas as pd

# GoogleNewsの単語ベクトルを読み込む
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True
)

# モデルの情報を表示
print(f"語彙数: {len(model.key_to_index)}")
print(f"ベクトルの次元数: {model.vector_size}")

# 単語ベクトルを表示
word = "United_States"
if word in model:
    print(word,'の単語ベクトル：',model[word])

# データをDataFrameに変換
# data = [['love', 'sex', '6.77'], ['tiger', 'cat', '7.35'], ['tiger', 'tiger', '10.00']]  # 例データ
df = pd.DataFrame(data, columns=['word1', 'word2', 'human'])
print("\nDataFrame:")
print(df)
