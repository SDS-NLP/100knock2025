from collections import defaultdict

file_path = "popular-names.txt"

try:
    frequency = defaultdict(int)  
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            name = line.split('\t')[0]
            frequency[name] += 1  

    
    sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    print("出現頻度\t名前")
    for name, count in sorted_freq:
        print(f"{count}\t{name}")  #

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")