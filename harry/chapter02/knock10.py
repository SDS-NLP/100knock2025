# count_lines.py

import sys

def count_lines(file_path):
    """指定されたファイルの行数を数える関数"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
        return None

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python count_lines.py ファイル名")
        sys.exit(1)

    file_path = sys.argv[1]
    line_count = count_lines(file_path)

    if line_count is not None:
        print(f"{file_path} の行数: {line_count}")

# unix command
# wc -l popular-names.txt