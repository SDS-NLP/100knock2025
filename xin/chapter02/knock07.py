# ファイルの1列目のユニークな文字列を取得する関数
def get_unique_values_in_first_column(filepath):
    unique_values = set()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            # 各行をスペースで分割して1列目を取得
            columns = line.split()
            if columns:  # 空行を無視
                unique_values.add(columns[0])
    return unique_values

file_path = '/home/tanxin/100knock2025/xin/chapter02/popular-names.txt'
unique_values = get_unique_values_in_first_column(file_path)
print("1列目のユニークな文字列:")
print("\n".join(sorted(unique_values)))