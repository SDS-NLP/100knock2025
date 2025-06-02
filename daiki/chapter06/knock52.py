from gensim.models import KeyedVectors

# モデルのパス
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'

# モデルの読み込み
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# 類似語トップ10を取得
target_word = 'United_States'

#model.most_similar()はコサイン類似度が高い順に似た単語を返す
#[(単語, 類似度), ...]のリストを返す
similar_words = model.most_similar(target_word, topn=10)
    
print(f"「{target_word}」とコサイン類似度が高い単語トップ10：\n")
for word, similarity in similar_words:
    print(f"{word:<20} 類似度: {similarity:.4f}")
#{word:<20}は左詰め20文字の幅に整形

#出力結果
"""「United_States」とコサイン類似度が高い単語トップ10：

Unites_States        類似度: 0.7877
Untied_States        類似度: 0.7541
United_Sates         類似度: 0.7401
U.S.                 類似度: 0.7311
theUnited_States     類似度: 0.6404
America              類似度: 0.6178
UnitedStates         類似度: 0.6167
Europe               類似度: 0.6133
countries            類似度: 0.6045
Canada               類似度: 0.6019"""