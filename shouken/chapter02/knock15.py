#ファイルを行単位でN分割し、別のファイルに格納せよ。例えば、N=10としてファイルを10分割せよ。同様の処理をsplitコマンドで実現せよ。

file_path = "popular-names.txt"
num_splits = 10

def count_lines(file_path):
    line_count = 0
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line_count += 1
    return line_count

def split_file(file_path, num_splits):
    total_lines = count_lines(file_path)

    lines_per_file = total_lines // num_splits
    if total_lines % num_splits != 0:
        lines_per_file += 1

    with open(file_path, 'r', encoding='utf-8') as input_file:
        for file_index in range(num_splits):
            output_filename = f"split_{file_index + 1}.txt"

            with open(output_filename, 'w', encoding='utf-8') as output_file:
                for _ in range(lines_per_file):
                    line = input_file.readline()

                    if not line:
                        break

                    output_file.write(line)

split_file(file_path, num_splits)

# wc -l popular-names.txt
# split -l 278 popular-names.txt split_

