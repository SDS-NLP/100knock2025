import random

file_path = "popular-names.txt"
output_path = "shuffled-popular-names.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()  

    random.shuffle(lines)  

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)  

    print("ランダム並び替え完了")

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")