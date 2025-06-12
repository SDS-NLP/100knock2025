import gensim.downloader as api
import urllib.request

# --- モデルロード ---
print("Loading model...")
model = api.load("glove-wiki-gigaword-100")
print("Model loaded.")

# --- データダウンロード ---
url = "https://raw.githubusercontent.com/RaRe-Technologies/gensim/develop/gensim/test/test_data/questions-words.txt"
local_path = "questions-words.txt"
urllib.request.urlretrieve(url, local_path)
print("questions-words.txt downloaded.")

# --- セクション分類用 ---
semantic_sections = {
    "capital-common-countries",
    "capital-world",
    "currency",
    "city-in-state",
    "family"
}

syntactic_sections = {
    "gram1-adjective-to-adverb",
    "gram2-opposite",
    "gram3-comparative",
    "gram4-superlative",
    "gram5-present-participle",
    "gram6-nationality-adjective",
    "gram7-past-tense",
    "gram8-plural",
    "gram9-plural-verbs"
}

# --- 集計 ---
semantic_total = semantic_correct = 0
syntactic_total = syntactic_correct = 0

with open(local_path, encoding="utf-8") as f:
    current_section = None
    for line in f:
        if line.startswith(":"):
            current_section = line.strip()[2:]
            continue

        if current_section is None:
            continue

        parts = line.strip().lower().split()
        if len(parts) != 4:
            continue
        w1, w2, w3, actual = parts

        if all(word in model for word in (w1, w2, w3)):
            vec = model[w2] - model[w1] + model[w3]
            predicted, _ = model.similar_by_vector(vec, topn=1)[0]

            is_correct = (predicted == actual)

            if current_section in semantic_sections:
                semantic_total += 1
                if is_correct:
                    semantic_correct += 1
            elif current_section in syntactic_sections:
                syntactic_total += 1
                if is_correct:
                    syntactic_correct += 1

# --- 結果出力 ---
semantic_accuracy = semantic_correct / semantic_total if semantic_total else 0
syntactic_accuracy = syntactic_correct / syntactic_total if syntactic_total else 0

print(f"\n意味的アナロジー（semantic）正解率: {semantic_accuracy:.2%}  ({semantic_correct}/{semantic_total})")
print(f"文法的アナロジー（syntactic）正解率: {syntactic_accuracy:.2%}  ({syntactic_correct}/{syntactic_total})")
