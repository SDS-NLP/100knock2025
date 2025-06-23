import gensim.downloader as api

print(list(api.info()['models'].keys()))

model = api.load("glove-wiki-gigaword-100")

# 単語ベクトル表示
print(model['u.s.'][:10])