# replace_tab_with_space.py

import sys

def show_head_with_spaces(file_path, n=10):
    """ファイルの先頭n行を表示し、タブをスペースに置換する"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= n:
                    break
                print(line.replace('\t', ' ').rstrip())
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python replace_tab_with_space.py ファイル名")
        sys.exit(1)

    file_path = sys.argv[1]
    show_head_with_spaces(file_path)

# unix command
# head -n 10 popular-names.txt | sed 's/\t/ /g'