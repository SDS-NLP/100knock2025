import subprocess
# ファイルの末尾N行を取得する関数
def get_last_n_lines(filepath, n):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines[-n:]

# tailコマンドを用いて末尾N行を取得する関数
def get_last_n_lines_with_tail(filepath, n):
    result = subprocess.run(['tail', '-n', str(n), filepath], stdout=subprocess.PIPE, text=True)
    return result.stdout

# ファイルパスと行数を指定
file_path = '/home/tanxin/100knock2025/xin/chapter02/popular-names.txt'
N = 10

# Pythonで取得
python_lines = get_last_n_lines(file_path, N)
print("Pythonで取得した末尾10行:")
print("".join(python_lines))

# tailコマンドで取得
tail_lines = get_last_n_lines_with_tail(file_path, N)
print("\ntailコマンドで取得した末尾10行:")
print(tail_lines)

# 一致しているか確認
if "".join(python_lines) == tail_lines:
    print("結果が一致しました！")
else:
    print("結果が一致しませんでした。")