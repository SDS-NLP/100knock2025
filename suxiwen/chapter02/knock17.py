file_path = "popular-names.txt"

try:
    unique_names = set()  
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            name = line.split('\t')[0]  
            unique_names.add(name) 

    print(f"1列目の異なる文字列の数: {len(unique_names)}")
    for name in unique_names:
        print(name)  

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")