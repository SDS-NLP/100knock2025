from gensim.models import KeyedVectors

# モデルの読み込み
model_path = '/Users/aa/GoogleNews-vectors-negative300.bin'
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# アナロジーデータのパス
analogy_path = '/Users/aa/questions-words.txt'

# セクション分類
semantic_sections = {
    'capital-common-countries',
    'capital-world',
    'currency',
    'city-in-state',
    'family'
}

syntactic_sections = {
    'gram1-adjective-to-adverb',
    'gram2-opposite',
    'gram3-comparative',
    'gram4-superlative',
    'gram5-present-participle',
    'gram6-nationality-adjective',
    'gram7-past-tense',
    'gram8-plural',
    'gram9-plural-verbs'
}

# 結果格納用
score = {
    'semantic': {'correct': 0, 'total': 0},
    'syntactic': {'correct': 0, 'total': 0}
}

# アナロジーテスト実行
with open(analogy_path, 'r', encoding='utf-8') as f:
    category = None
    for line in f:
        line = line.strip()

        if line.startswith(':'):
            section = line[2:].strip()
            if section in semantic_sections:
                category = 'semantic'
            elif section in syntactic_sections:
                category = 'syntactic'
            else:
                category = None  # その他のセクションはスキップ
            continue

        if category:
            a, b, c, d = line.split()
            if all(w in model for w in [a, b, c]):
                predicted, _ = model.most_similar(positive=[b, c], negative=[a], topn=1)[0]
                if predicted.lower() == d.lower():
                    score[category]['correct'] += 1
                score[category]['total'] += 1

# 結果出力
for category in ['semantic', 'syntactic']:
    correct = score[category]['correct']
    total = score[category]['total']
    accuracy = correct / total if total > 0 else 0
    print(f"{category.capitalize()} analogy accuracy: {accuracy:.2%} ({correct}/{total})")