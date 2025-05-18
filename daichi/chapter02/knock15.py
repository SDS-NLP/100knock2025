
N = 10  # 分割数
lines = []

# ファイルを読み込む
with open('./daichi/chapter02/popular-names.txt') as f:
    lines = f.readlines()

# 総行数
total_lines = len(lines)
# 1つのファイルに入れる行数（できるだけ均等に）
lines_per_file = total_lines // N + (1 if total_lines % N != 0 else 0)

# 分割して保存
for i in range(N):
    start = i * lines_per_file
    end = start + lines_per_file
    chunk = lines[start:end]
    with open(f'./daichi/chapter02/split_{i}.txt', 'w') as f_out:
        f_out.writelines(chunk)
