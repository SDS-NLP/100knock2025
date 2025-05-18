# shuffle_lines.py

import sys
import random

def shuffle_file_lines(file_path):
    """ファイルの行をランダムに並び替えて表示する（内容は変更しない）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
        return

    random.shuffle(lines)

    for line in lines:
        print(line.rstrip())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python shuffle_lines.py ファイル名")
        sys.exit(1)

    file_path = sys.argv[1]
    shuffle_file_lines(file_path)

# unix command
# shuf popular-names.txt
# shuf popular-names.txt > shuffled.txt