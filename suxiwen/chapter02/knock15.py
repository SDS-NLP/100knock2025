file_path = "popular-names.txt"
n = 10  # 分割数

try:
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        total_lines = len(lines)
        lines_per_part = total_lines // n + (1 if total_lines % n != 0 else 0)  

        for i in range(n):
            start = i * lines_per_part
            end = start + lines_per_part
            part_lines = lines[start:end]
            output_file = f"part_{i+1}.txt" 

            with open(output_file, "w", encoding="utf-8") as out_f:
                out_f.writelines(part_lines)  

            print(f"{output_file} を作成（行数: {len(part_lines)}）")

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")