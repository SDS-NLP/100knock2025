from gensim.models import KeyedVectors
from collections import defaultdict

# モデル読み込み
model_path = "GoogleNews-vectors-negative300.bin.gz"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)

# semantic / syntactic セクションの定義
semantic_sections = {
    "capital-common-countries", "capital-world", "currency",
    "city-in-state", "family"
}
syntactic_sections = {
    "adjective-to-adverb", "opposite", "comparative",
    "superlative", "present-participle", "nationality-adjective",
    "past-tense", "plural", "plural-verbs"
}

# 結果集計用
results = defaultdict(lambda: {"correct": 0, "total": 0})

# アナロジーファイル読み込み
analogy_path = "questions-words.txt"
current_section = None

with open(analogy_path, encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if line.startswith(":"):
            current_section = line[2:]
            continue
        if current_section is None:
            continue

        try:
            a, b, c, d = line.lower().split()
            predicted = model.most_similar(positive=[b, c], negative=[a], topn=1)[0][0]
            is_correct = (predicted.lower() == d.lower())
        except KeyError:
            is_correct = False  # 語彙外は不正解として扱う

        # セクションに応じて分類
        if current_section in semantic_sections:
            category = "semantic"
        elif current_section in syntactic_sections:
            category = "syntactic"
        else:
            continue  # その他のセクションは無視

        results[category]["total"] += 1
        if is_correct:
            results[category]["correct"] += 1

# 正解率表示
for cat in ["semantic", "syntactic"]:
    total = results[cat]["total"]
    correct = results[cat]["correct"]
    acc = correct / total if total > 0 else 0.0
    print(f"{cat.capitalize()} Analogy Accuracy: {acc:.4f} ({correct}/{total})")
