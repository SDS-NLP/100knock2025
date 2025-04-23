import subprocess

# ファイルの行数をカウントする関数
def count_lines(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return len(lines)

# wcコマンドを用いて行数を取得する関数
def count_lines_with_wc(filepath):
    result = subprocess.run(['wc', '-l', filepath], stdout=subprocess.PIPE, text=True)
    # 出力例: "10 filename.txt" -> 10 を抽出
    return int(result.stdout.split()[0])

content= "popular-names.txt"

print(content)

# Pythonでカウント
python_count = count_lines(content)
print(f"Pythonでカウントした行数: {python_count}")

# wcコマンドでカウント
wc_count = count_lines_with_wc(content)
print(f"wcコマンドでカウントした行数: {wc_count}")

# 一致しているか確認
if python_count == wc_count:
    print("行数が一致しました！")
else:
    print("行数が一致しませんでした。")