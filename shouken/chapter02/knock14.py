file_path = "popular-names.txt"
n = 10

def extract_first_column(file_path, n):
    with open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            if i >= n:
                break
            columns = line.rstrip().split('\t') 
            print(columns[0])

extract_first_column(file_path, n)

# head -n 10 popular-names.txt | cut -f 1
