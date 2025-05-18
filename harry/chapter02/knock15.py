# split_by_lines.py

import sys
import math

def split_file(file_path, num_splits):
    """指定されたファイルを行単位で num_splits に分割する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
        return

    total_lines = len(lines)
    lines_per_file = math.ceil(total_lines / num_splits)

    for i in range(num_splits):
        start = i * lines_per_file
        end = min(start + lines_per_file, total_lines)
        chunk = lines[start:end]

        output_filename = f"split_{i}.txt"
        with open(output_filename, 'w', encoding='utf-8') as out_file:
            out_file.writelines(chunk)

        print(f"✅ {output_filename} に {len(chunk)} 行を書き込みました。")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使い方: python split_by_lines.py ファイル名 分割数")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        num_splits = int(sys.argv[2])
        if num_splits <= 0:
            raise ValueError
    except ValueError:
        print("❌ 分割数は1以上の整数で指定してください")
        sys.exit(1)

    split_file(file_path, num_splits)

# unix command
# total=$(wc -l < popular-names.txt)
# lines_per_file=$(( total / 10 ))  
# split -l $lines_per_file popular-names.txt split_
