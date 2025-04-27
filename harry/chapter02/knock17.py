# count_unique_column.py

import sys

def count_unique_values(file_path, column_index):
    """指定された列（0始まり）にあるユニークな値を数えて表示"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            unique_values = set()
            for line in f:
                columns = line.rstrip().split('\t')
                if len(columns) > column_index:
                    unique_values.add(columns[column_index])
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
        return

    print(f"🧮 列 {column_index + 1} の異なる値の数は {len(unique_values)} 個です。")
    print("📋 異なる値:")
    for value in sorted(unique_values):
        print(value)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使い方: python count_unique_column.py ファイル名 列番号（1から）")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        column_number = int(sys.argv[2])
        if column_number < 1:
            raise ValueError
        column_index = column_number - 1  # Pythonでは0始まり
    except ValueError:
        print("❌ 列番号は1以上の整数で指定してください")
        sys.exit(1)

    count_unique_values(file_path, column_index)

# unix command
# cut -f 2 popular-names.txt | sort | uniq
# cut -f 2 popular-names.txt | sort | uniq | wc -l