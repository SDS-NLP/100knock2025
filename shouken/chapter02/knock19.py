file_path = 'popular-names.txt'
output_path = 'popular-names_sorted.txt'

def get_third_column_as_number(line):

    columns = line.strip().split('\t')
    return float(columns[2])

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

lines.sort(key=get_third_column_as_number, reverse=True)

with open(output_path, 'w', encoding='utf-8') as f:
    f.writelines(lines)


# sort -k 3,3nr popular-names.txt > popular-names_sorted.txt
