file_path = "popular-names.txt"
output_path = "sorted-by-count.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

   
    lines.sort(key=lambda x: int(x.split('\t')[2]), reverse=True)

    with open(output_path, "w", encoding="utf-8") as f:
        f.writelines(lines)  

    print(f"3列目（人数）で降順ソート完了：{output_path}")

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")