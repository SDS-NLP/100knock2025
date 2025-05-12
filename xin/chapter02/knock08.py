from collections import Counter

# ファイルの1列目の出現頻度を取得する関数
def count_frequency_in_first_column(filepath):
    counter = Counter()
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            columns = line.split()
            if columns:  # 空行を無視
                counter[columns[0]] += 1
    return counter

# 出現頻度を多い順に表示する関数
def display_sorted_frequency(counter):
    sorted_frequency = sorted(counter.items(), key=lambda x: x[1], reverse=True)
    for name, count in sorted_frequency:
        print(f"{name}: {count}")

file_path = '/home/tanxin/100knock2025/xin/chapter02/popular-names.txt'
frequency_counter = count_frequency_in_first_column(file_path)
print("出現頻度（降順）:")
display_sorted_frequency(frequency_counter)