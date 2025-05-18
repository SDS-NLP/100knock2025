from collections import Counter

file_path = 'popular-names.txt'

names = []

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        name = line.strip().split('\t')[0]
        names.append(name)

counter = Counter(names)

for name, count in counter.most_common():
    print(count, name)

# cut -f 1 popular-names.txt | sort | uniq -c | sort -nr
