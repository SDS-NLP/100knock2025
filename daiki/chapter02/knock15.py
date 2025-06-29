file = "daiki/chapter02/popular-names.txt"
N = 10
with open(file, 'r') as r:
    lines = r.readlines()
    total_lines = len(lines)
    #１ファイルの行数
    lines_per_file = total_lines // N
    remainder = total_lines % N 
    
    for i in range(N):
        start = lines_per_file * i + min(remainder, i)
        #余りを考慮して行数調整
        end = start + lines_per_file + (1 if i < remainder else 0)
        #ファイルを作成
        output_file = f'output_{i}.txt'
        #ファイルに書き込み ('w'は書き込みの際に使うモード)
        with open(output_file, 'w') as w:
           w.writelines(lines[start:end])
        print(output_file)
#splitコマンド split -l $(( $(wc -l < daiki/chapter02/popular-names.txt) / 10)) daiki/chapter02/popular-names.txt output_
"""output_0.txt
output_1.txt
output_2.txt
output_3.txt
output_4.txt
output_5.txt
output_6.txt
output_7.txt
output_8.txt
output_9.txt"""#ファイル開けた