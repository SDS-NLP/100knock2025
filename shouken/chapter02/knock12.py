# ファイル名と、表示したい行数を設定
file_path = "popular-names.txt"
n = 10

def tail(file_path, n):

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    for line in lines[-n:]:
        print(line.rstrip())


tail(file_path, n)

# tail -n 10 popular-names.txt
