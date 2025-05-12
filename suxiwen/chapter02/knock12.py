n = 10  
file_path = "popular-names.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()  
        start_index = max(0, len(lines) - n)  
        for line in lines[start_index:]:
            print(line, end="")

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")