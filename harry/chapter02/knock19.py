# sort_by_column_desc.py

import sys

def sort_by_column_desc(file_path, column_index):
    """指定された列（0始まり）の数値でファイルの各行を降順ソート"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.rstrip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ ファイルが見つかりません: {file_path}")
        return

    try:
        # 指定列の数値で降順ソート（タブ区切り）
        sorted_lines = sorted(
            lines,
            key=lambda x: float(x.split('\t')[column_index]),
            reverse=True
        )
    except (IndexError, ValueError):
        print("❌ 整列に失敗しました。列番号やデータ形式を確認してください。")
        return

    for line in sorted_lines:
        print(line)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("使い方: python sort_by_column_desc.py ファイル名 列番号（1から）")
        sys.exit(1)

    file_path = sys.argv[1]
    try:
        column_number = int(sys.argv[2])
        if column_number < 1:
            raise ValueError
        column_index = column_number - 1  # Pythonのインデックスに変換（0始まり）
    except ValueError:
        print("❌ 列番号は1以上の整数で指定してください")
        sys.exit(1)

    sort_by_column_desc(file_path, column_index)

# unix command
# sort -k 3,3 -nr popular-names.txt