file_path = 'popular-names.txt'

names = set()

with open(file_path, 'r', encoding='utf-8') as f:
    for line in f:
        name = line.strip().split('\t')[0]
        names.add(name)

for name in sorted(names):
    print(name)


# cut -f 1 popular-names.txt | sort | uniq
