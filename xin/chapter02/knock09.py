import subprocess

# ファイルの3列目の数値で逆順に整列する関数
def sort_by_third_column_desc(filepath, output_filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 整列処理（3列目を基準に逆順）
    sorted_lines = sorted(lines, key=lambda line: float(line.split()[2]), reverse=True)
    
    # 整列結果をファイルに書き込み
    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        output_file.writelines(sorted_lines)

input_file = "/home/tanxin/100knock2025/xin/chapter02/popular-names.txt"
output_file = "sorted_popular_names.txt"
sort_by_third_column_desc(input_file, output_file)
print(f"3列目の数値で逆順に並び替えた結果を {output_file} に保存しました。")

# Linuxのsortコマンドを使用して3列目の数値で逆順に整列
subprocess.run(
    ["sort", "-k", "3,3", "-n", "-r", "/home/tanxin/100knock2025/xin/chapter02/popular-names.txt", "-o", "sorted_popular_names_sort.txt"],
    check=True
)
print("Linuxのsortコマンドを使用して3列目の数値で逆順に並び替えた結果を sorted_popular_names_sort.txt に保存しました。")