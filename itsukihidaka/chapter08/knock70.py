import numpy as np
from gensim.models import KeyedVectors
from tqdm import tqdm

# GoogleNewsの単語ベクトルを読み込む
print('--- modelロード中 ---')
model = KeyedVectors.load_word2vec_format(
    '/Users/itsukihidaka/Downloads/GoogleNews-vectors-negative300.bin.gz',
    binary=True
)
print('--- modelロード完了 ---')

# モデルに含まれる全ての単語を取得
all_words = list(model.key_to_index.keys())
words_list = ['<PAD>'] + all_words
E = np.zeros((len(words_list), 300))
word_to_index = {"<PAD>": 0}
index_to_word = {0: "<PAD>"}

for i, word in tqdm(enumerate(all_words)):
    E[i+1] = model[word]
    word_to_index[word] = i+1
    index_to_word[i+1] = word

print('E,word_to_index,index_to_wordの作成完了')

if __name__ == "__main__":
    print(E)
    print(len(E))
    print(word_to_index)
    print(index_to_word)

