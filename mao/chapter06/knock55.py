"""
knock55:アナロジータスクでの正解率
54の実行結果を用い、意味的アナロジー（semantic analogy）と
文法的アナロジー（syntactic analogy）の正解率を測定せよ。
"""
from knock54 import results, section_list
from collections import defaultdict

accuracy_stats = {
    "semantic": {"correct": 0, "total": 0},
    "syntactic": {"correct": 0, "total": 0}
}

def get_section_type(section_name):
    if section_name.startswith("gram"):
        return "syntactic"
    else:
        return "semantic"

for (A, B, C, D, predicted, _), section in zip(results, section_list):
    section_type = get_section_type(section)
    accuracy_stats[section_type]["total"] += 1
    if predicted == D:
        accuracy_stats[section_type]["correct"] += 1

for kind in ["semantic", "syntactic"]:
    correct = accuracy_stats[kind]["correct"]
    total = accuracy_stats[kind]["total"]
    acc = correct / total if total > 0 else 0.0
    print(f"{kind.capitalize()} analogy accuracy: {acc:.3%} ({correct}/{total})")

na_count = 0

for (A, B, C, D, predicted, _), section in zip(results, section_list):
    section_type = get_section_type(section)
    accuracy_stats[section_type]["total"] += 1
    if predicted == "N/A":
        na_count += 1
        continue
    if predicted == D:
        accuracy_stats[section_type]["correct"] += 1

print(f"N/A predictions: {na_count}")
