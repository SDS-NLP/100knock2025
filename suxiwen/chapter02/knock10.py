file_path = "popular-names.txt"

try:
    with open(file_path, "r", encoding="utf-8") as f:
        line_count = sum(1 for _ in f)  # 1行ごとにカウント
    print(f"ファイルの行数: {line_count}")

except FileNotFoundError:
    print(f"エラー: {file_path} が見つかりません。")