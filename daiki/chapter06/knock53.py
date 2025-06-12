from gensim.models import KeyedVectors

# モデルのパス
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'

# モデルの読み込み
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 単語を指定
positive = ['Athens', 'Spain']
negative = ['Madrid']

results = model.most_similar(positive=positive, negative=negative, topn=10)
    
print(f"Spain - Madrid + Athens に最も近い単語トップ10：\n")
for word, score in results:
    print(f"{word:<25} 類似度: {score:.4f}")

#出力結果：
"""Spain - Madrid + Athens に最も近い単語トップ10：

Greece                    類似度: 0.6898
Aristeidis_Grigoriadis    類似度: 0.5607
Ioannis_Drymonakos        類似度: 0.5553
Greeks                    類似度: 0.5451
Ioannis_Christou          類似度: 0.5401
Hrysopiyi_Devetzi         類似度: 0.5248
Heraklio                  類似度: 0.5208
Athens_Greece             類似度: 0.5169
Lithuania                 類似度: 0.5167
Iraklion                  類似度: 0.5147"""