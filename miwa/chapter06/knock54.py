#54. アナロジーデータでの実験
from knock50 import model
from collections import defaultdict


path = "questions-words.txt"
results = defaultdict(list)
with open(path, "r", encoding="utf-8") as f:
    for line in f:
        # セクション見出し行に対する処理
        if line.startswith(":"):
            if "capital-common-countries" in line:
                continue  
            else:
                break
        else:
            fields = line.strip().split()
            new_vec = model[fields[1]] - model[fields[0]] + model[fields[2]]
            result = model.most_similar(new_vec, topn=1) 
            results[f"{fields[1]} - {fields[0]} + {fields[2]}:"].append(result)

for key, value in results.items():
    print(key, value)
