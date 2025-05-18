n = 10  # 処理する行数
file_path = "popular-names.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for _ in range(n):
            line = f.readline()
            first_column = line.split('\t')[0]  
            print(first_column)  

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")