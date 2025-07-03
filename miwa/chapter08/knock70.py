#70. 単語埋め込みの読み込み
from gensim.models import KeyedVectors
import numpy as np

embedding_path = "chapter06/GoogleNews-vectors-negative300.bin.gz"

print("Word2Vecモデルを読み込み")
model = KeyedVectors.load_word2vec_format(embedding_path, binary=True)
print("モデル読み込み完了")

d_emb = model.vector_size  # 埋め込みの次元（GoogleNewsは300）
word2id = {'<PAD>': 0}  #語彙→idに変換できる辞書、<PAD>のidを0に設定
id2word = {0: '<PAD>'}  #id→語彙に変換できる辞書、id0は<PAD>
embedding_vectors = [np.zeros(d_emb, dtype=np.float32)]  # E[0] ← ゼロベクトル


# 語彙を順番に追加（max_vocab_size で制限）
max_vocab_size=50000 #語彙数制限　全部取り出したら多すぎるから
for i, word in enumerate(model.index_to_key): #model.index_to_keyで語彙を出現頻度順に取り出す
    if max_vocab_size and len(word2id) >= max_vocab_size:
        break
    vector = model[word]
    idx = len(word2id)
    word2id[word] = idx
    id2word[idx] = word
    embedding_vectors.append(vector)

#リスト形式のembeddig_vectorsから二次元の行列を作る
E = np.vstack(embedding_vectors)

if __name__ == "__maina__":
    print(f"語彙数（<PAD>含む）: {E.shape[0]}")
    print(f"埋め込み次元: {E.shape[1]}")
    #print(E, word2id, id2word)

