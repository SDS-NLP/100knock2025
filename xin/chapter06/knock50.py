import gensim.downloader as api

# モデルの一覧表示（任意）
print(list(api.info()['models'].keys()))

# 軽量の GloVe モデル（100次元）をロード
model = api.load("glove-wiki-gigaword-100")
#print('u.s.' in model)  # Falseなら辞書にない
# 単語ベクトル表示
print(model['u.s.'][:10])
