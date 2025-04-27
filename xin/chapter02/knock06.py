import random

# ファイル内の行をランダムに並び替える関数
def shuffle_lines(filepath, output_filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    random.shuffle(lines)  # 行をランダムに並び替え
    with open(output_filepath, 'w', encoding='utf-8') as output_file:
        output_file.writelines(lines)

input_file = '/home/tanxin/100knock2025/xin/chapter02/popular-names.txt'
output_file = 'shuffled_popular-names.txt'
shuffle_lines(input_file, output_file)
print(f"ランダムに並び替えた結果を {output_file} に保存しました。")