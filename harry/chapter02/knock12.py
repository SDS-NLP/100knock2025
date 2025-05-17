# show_tail.py

import sys

def show_tail(file_path, n):
    """指定されたファイルの末尾n行を表示する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines[-n:]:
                print(line.rstrip())
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
    except ValueError:
        print("❌ 行数は整数で指定してください")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使い方: python show_tail.py ファイル名 行数")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        n_lines = int(sys.argv[2])
    except ValueError:
        print("❌ 行数は整数で指定してください")
        sys.exit(1)

    show_tail(file_path, n_lines)

# unix command
# tail -n 10 popular-names.txt