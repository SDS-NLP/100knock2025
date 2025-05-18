file_path = "popular-names.txt"
n = 10

def replace_tab_with_space(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            print(line.replace('\t', ' ').rstrip())

replace_tab_with_space(file_path, n)