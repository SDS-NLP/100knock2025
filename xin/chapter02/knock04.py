import subprocess

# ファイルの先頭10行の1列目だけを取得する関数
def get_first_column(filepath, n):
    first_column = []
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()[:n]
        for line in lines:
            # 各行をスペースで分割して1列目を取得
            first_column.append(line.split()[0])
    return first_column

# cutコマンドを使用して先頭10行の1列目を取得する関数
def get_first_column_with_cut(filepath, n):
    result = subprocess.run(
        ['head', f'-n{n}', filepath], stdout=subprocess.PIPE, text=True
    )
    # headの結果をcutで1列目だけ抽出
    cut_result = subprocess.run(
        ['cut', '-d', ' ', '-f1'], input=result.stdout, stdout=subprocess.PIPE, text=True
    )
    return cut_result.stdout.splitlines()

# ファイルパスと行数を指定
file_path = "/home/tanxin/100knock2025/xin/chapter02/popular-names.txt"
N = 10

# Pythonで1列目を抽出
python_result = get_first_column(file_path, N)
print("Pythonで取得した1列目:")
print("\n".join(python_result))

# cutコマンドで1列目を抽出
cut_result = get_first_column_with_cut(file_path, N)
print("\ncutコマンドで取得した1列目:")
print("\n".join(cut_result))

# 結果の一致を確認
if python_result == cut_result:
    print("\n結果が一致しました！")
else:
    print("\n結果が一致しませんでした。")