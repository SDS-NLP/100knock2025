import os

# ファイルを行単位でN分割する関数
def split_file(filepath, n):
    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    # 1ファイルあたりの行数を計算
    chunk_size = len(lines) // n
    remainder = len(lines) % n
    
    # 分割してファイルに書き込む
    for i in range(n):
        start = i * chunk_size + min(i, remainder)
        end = start + chunk_size + (1 if i < remainder else 0)
        chunk_lines = lines[start:end]
        
        # 分割ファイルの名前を設定
        output_filename = f"split_{i+1}.txt"
        with open(output_filename, 'w', encoding='utf-8') as output_file:
            output_file.writelines(chunk_lines)
        print(f"{output_filename} に書き込みました。")

file_path ='/home/tanxin/100knock2025/xin/chapter02/popular-names.txt'
N = 10
split_file(file_path, N)