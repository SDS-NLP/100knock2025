# 70. 単語埋め込みの読み込み
# 事前学習済み単語埋め込みを活用し、
# ｜V｜ x dembの単語埋め込み行列Eを作成せよ。
# ここで、｜V｜は単語埋め込みの語彙数、dembは単語埋め込みの次元数である。
# ただし、単語埋め込み行列の先頭の行ベクトルE0は、
# 将来的にパディング（<PAD>）トークンの埋め込みベクトルとして用いたいので、ゼロベクトルとして予約せよ。ゆえに、
# Eの2行目以降に事前学習済み単語埋め込みを読み込むことになる。
# もし、Google Newsデータセットの学習済み単語ベクトル（300万単語・フレーズ、300次元）を全て読み込んだ場合、
# ｜V｜= 3000001,demb=300になるはずである（ただ、300万単語の中には、殆ど用いられない稀な単語も含まれるので、語彙を削減した方がメモリの節約になる）。
# また、単語埋め込み行列の構築と同時に、単語埋め込み行列の各行のインデックス番号（トークンID）と、単語（トークン）への双方向の対応付けを保持せよ。

# knock70.py
import numpy as np
import re
from collections import Counter
import gensim.downloader as api
import os
import torch

# -----------------------------
# 設定
# -----------------------------
EMBED_DIM = 100
MAX_VOCAB = 50000
USE_UNK = True
tsv_base_path = os.path.join("..", "chapter07", "SST-2")

# -----------------------------
# トークナイザー
# -----------------------------
def tokenize(text):
    return re.findall(r'\b\w+\b', text.lower())

# -----------------------------
# 使用語彙の収集
# -----------------------------
vocab_counter = Counter()
for name in ['train.tsv', 'dev.tsv', 'test.tsv']:
    file_path = os.path.join(tsv_base_path, name)
    with open(file_path, encoding='utf-8') as f:
        next(f)  # ヘッダーをスキップ
        for line in f:
            parts = line.strip().split('\t')
            text = parts[1] if name == 'test.tsv' else parts[0]
            tokens = tokenize(text)
            vocab_counter.update(tokens)

used_vocab = set([w for w, _ in vocab_counter.most_common(MAX_VOCAB)])

# -----------------------------
# GloVeモデルの読み込み
# -----------------------------
print("📥 Loading GloVe vectors...")
model = api.load("glove-wiki-gigaword-100")

# -----------------------------
# 埋め込み行列の初期化
# -----------------------------
embedding_matrix = []
word2id = {}
id2word = {}

# <PAD>
word2id["<PAD>"] = 0
id2word[0] = "<PAD>"
embedding_matrix.append(np.zeros(EMBED_DIM, dtype=np.float32))

# <UNK>
if USE_UNK:
    word2id["<UNK>"] = 1
    id2word[1] = "<UNK>"
    embedding_matrix.append(np.random.uniform(-0.25, 0.25, EMBED_DIM).astype(np.float32))

# -----------------------------
# 語彙の追加
# -----------------------------
for word in used_vocab:
    if word in model:
        idx = len(word2id)
        word2id[word] = idx
        id2word[idx] = word
        embedding_matrix.append(model[word])

embedding_matrix = np.stack(embedding_matrix)

# -----------------------------
# 情報表示
# -----------------------------
print(f"✅ 語彙数（<PAD>{' + <UNK>' if USE_UNK else ''} 含む）: {len(word2id)}")
print(f"✅ 埋め込み行列の形状: {embedding_matrix.shape}")

# -----------------------------
# 保存
# -----------------------------
torch.save(torch.tensor(embedding_matrix), 'embedding.pt')
torch.save(word2id, 'word2id.pt')
print("💾 'embedding.pt' と 'word2id.pt' を保存しました。")


