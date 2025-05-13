import random

file_path = 'popular-names.txt'
output_path = 'popular-names_shuffled.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

random.shuffle(lines)

with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)


# shuf popular-names.txt > popular-names_shuffled.txt
