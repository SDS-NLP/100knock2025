#50.単語ベクトルの読み込みと表示
import gensim

model = gensim.models.KeyedVectors.load_word2vec_format(
    "GoogleNews-vectors-negative300.bin.gz", binary=True
)
if __name__ == "__main__":
    result = model["United_States"] #ここで単語を指定
    print(result)