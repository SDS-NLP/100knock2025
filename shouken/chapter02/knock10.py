file_path = "popular-names.txt"

def count_lines(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        count = sum(1 for _ in f)
    return count

print(count_lines(file_path)) 

# 確認にはwcコマンドを用いよ
# wc -l popular-names.txt
# 2780 popular-names.txt