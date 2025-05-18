import subprocess

# ファイルの先頭N行を取得する関数
def get_first_n_lines(filepath, n):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return lines[:n]

# headコマンドを用いて先頭N行を取得する関数
def get_first_n_lines_with_head(filepath, n):
    result = subprocess.run(['head', '-n', str(n), filepath], stdout=subprocess.PIPE, text=True)
    return result.stdout

file_path = "/home/tanxin/100knock2025/xin/chapter02/popular-names.txt"
N = 10

python_lines = get_first_n_lines(file_path, N)
print("Pythonで取得した先頭10行:")
print("".join(python_lines))

head_lines = get_first_n_lines_with_head(file_path, N)
print("\nheadコマンドで取得した先頭10行:")
print(head_lines)

if "".join(python_lines) == head_lines:
    print("結果が一致しました！")
else:
    print("結果が一致しませんでした。")