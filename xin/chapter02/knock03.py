import subprocess

# ファイルの先頭10行を取得し、タブをスペースに置換する関数
def replace_tabs_with_spaces(filepath, n):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()[:n]
        return [line.replace('\t', ' ') for line in lines]

# sedコマンドでタブをスペースに置換した先頭10行を取得する関数
def replace_tabs_with_spaces_sed(filepath, n):
    result = subprocess.run(
        ['sed', '-n', f'1,{n}p', filepath], stdout=subprocess.PIPE, text=True
    )
    sed_output = result.stdout.replace('\t', ' ')
    return sed_output

# ファイルパスと行数を指定
file_path = "/home/tanxin/100knock2025/xin/chapter02/popular-names.txt"
N= 10


# Pythonでタブを置換
python_lines = replace_tabs_with_spaces(file_path, N)
print("Pythonで処理した先頭10行（タブ→スペース）:")
print("".join(python_lines))

# sedコマンドでタブを置換
sed_lines = replace_tabs_with_spaces_sed(file_path, N)
print("\nsedコマンドで処理した先頭10行（タブ→スペース）:")
print(sed_lines)

# 結果の一致を確認
if "".join(python_lines) == sed_lines:
    print("結果が一致しました！")
else:
    print("結果が一致しませんでした。")