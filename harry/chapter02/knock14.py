# extract_first_column.py

import sys

def extract_first_column(file_path, n=10):
    """ファイルの先頭n行の1列目だけを表示する（タブ区切り）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= n:
                    break
                columns = line.rstrip().split('\t')
                if columns:
                    print(columns[0])
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使い方: python extract_first_column.py ファイル名")
        sys.exit(1)

    file_path = sys.argv[1]
    extract_first_column(file_path)

# unix command
# head -n 10 popular-names.txt | cut -f 1