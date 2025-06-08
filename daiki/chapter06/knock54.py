from gensim.models import KeyedVectors

# モデルのパス
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'

# モデルの読み込み
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# アナロジーファイル読み込み
analogy_path = '/Users/aa/questions-words.txt'  
section = 'capital-common-countries'

results = []

with open(analogy_path, 'r', encoding='utf-8') as f:
    reading = False
    for line in f:
        line = line.strip()

        # セクション切り替え検出
        if line.startswith(':'):
            reading = (line[2:].strip() == section)
            continue

        if reading:
            a, b, c, d = line.split()
            if all(w in model for w in [a, b, c]):
                predicted, similarity = model.most_similar(positive=[b, c], negative=[a], topn=1)[0]
                results.append((a, b, c, d, predicted, similarity))

# 結果表示（最初の10件）
for a, b, c, d, pred, sim in results[:10]:
    print(f"{a:<10} {b:<10} {c:<10} → {pred:<10}（正解: {d}） 類似度: {sim:.4f}")

#出力結果
"""Athens     Greece     Baghdad    → Iraqi     （正解: Iraq） 類似度: 0.6352
Athens     Greece     Bangkok    → Thailand  （正解: Thailand） 類似度: 0.7138
Athens     Greece     Beijing    → China     （正解: China） 類似度: 0.7236
Athens     Greece     Berlin     → Germany   （正解: Germany） 類似度: 0.6735
Athens     Greece     Bern       → Switzerland（正解: Switzerland） 類似度: 0.4920
Athens     Greece     Cairo      → Egypt     （正解: Egypt） 類似度: 0.7528
Athens     Greece     Canberra   → Australia （正解: Australia） 類似度: 0.5837
Athens     Greece     Hanoi      → Viet_Nam  （正解: Vietnam） 類似度: 0.6276
Athens     Greece     Havana     → Cuba      （正解: Cuba） 類似度: 0.6461
Athens     Greece     Helsinki   → Finland   （正解: Finland） 類似度: 0.6900"""