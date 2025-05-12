n = 10  
file_path = "popular-names.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        for _ in range(n):
            line = f.readline().replace("\t", " ")  
            print(line, end="")  

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")