#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gensim.models import KeyedVectors
from scipy.stats import spearmanr

# もデリのパスを指定
model_path = "/Users/niaomuqing/100knock2025/GoogleNews-vectors-negative300.bin"
model = KeyedVectors.load_word2vec_format(model_path, binary=True)
print("Model loaded.")

# ファイルパスを指定
analogy_file = "/Users/niaomuqing/100knock2025/questions-words.txt"

# 语义类和语法类 section 分类
semantic_sections = {
    ": capital-common-countries",
    ": capital-world",
    ": currency",
    ": city-in-state",
    ": family"
}

syntactic_sections = {
    ": gram1-adjective-to-adverb",
    ": gram2-opposite",
    ": gram3-comparative",
    ": gram4-superlative",
    ": gram5-present-participle",
    ": gram6-nationality-adjective",
    ": gram7-past-tense",
    ": gram8-plural",
    ": gram9-plural-verbs"
}

results = {}
current_section = None
oov_log = []

# 主处理流程
with open(analogy_file, "r", encoding="utf-8") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if i % 50 == 0:
            print(f"{i} lines processed...")

        if line.startswith(":"):
            current_section = line
            results[current_section] = {"correct": 0, "total": 0}
            print(f"\n[Section] {current_section}")
            continue

        if current_section is None:
            continue

        try:
            w1, w2, w3, w4 = line.split()
        except ValueError:
            continue  # skip malformed lines

        if all(w in model for w in [w1, w2, w3]):
            try:
                predicted, _ = model.most_similar(
                    positive=[w2, w3],
                    negative=[w1],
                    topn=1,
                    restrict_vocab=100000  # ← 提速关键
                )[0]
                if predicted.lower() == w4.lower():
                    results[current_section]["correct"] += 1
            except Exception as e:
                oov_log.append((w1, w2, w3, f"error: {e}"))
        else:
            oov_log.append((w1, w2, w3, "OOV"))

        results[current_section]["total"] += 1

# 统计正解率
semantic_correct = semantic_total = 0
syntactic_correct = syntactic_total = 0

for section, score in results.items():
    acc = score["correct"] / score["total"] if score["total"] > 0 else 0.0
    print(f"{section:<35} Accuracy: {acc:.4f} ({score['correct']}/{score['total']})")

    if section in semantic_sections:
        semantic_correct += score["correct"]
        semantic_total += score["total"]
    elif section in syntactic_sections:
        syntactic_correct += score["correct"]
        syntactic_total += score["total"]

# 输出最终汇总
print("\n--- Summary ---")
semantic_acc = semantic_correct / semantic_total if semantic_total > 0 else 0.0
syntactic_acc = syntactic_correct / syntactic_total if syntactic_total > 0 else 0.0
print(f"Semantic Analogy Accuracy : {semantic_acc:.4f} ({semantic_correct}/{semantic_total})")
print(f"Syntactic Analogy Accuracy: {syntactic_acc:.4f} ({syntactic_correct}/{syntactic_total})")

# 显示 OOV/异常
print(f"\nTotal OOV or error cases: {len(oov_log)}")


# In[ ]:




