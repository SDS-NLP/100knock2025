"""
knock50: 単語ベクトルの読み込みと表示
Google Newsデータセット(約1000億単語)での学習済みベクトルを
ダウンロードし、"United States"単語ベクトルを表示せよ。
ただし、"United States"内部には"United_States"と表示されていることに注意
"""
#学習機能は含まず、読み込み・検索・類似度計算に特化
from gensim.models import KeyedVectors

#モデルの読み込み
model_path="mao/chapter06/GoogleNews-vectors-negative300.bin"
model=KeyedVectors.load_word2vec_format(model_path,binary=True)

#対象の単語 #knock51用も含む
word_list=["United_States","U.S."]
vectors={}
for word in word_list:
    #ベクトル表示
    if word in model:
        vectors[word]=model[word]  #該当単語のベクトル(数値のリスト,300次元)を取り出す
        if __name__=="__main__":
            print(f"Vector for {word}:\n{vectors[word]}") #戻り値:np.ndarray
            print()
    else:
         if __name__=="__main__":
            print(f"not in the vocabulary.")