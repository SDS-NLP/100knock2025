#ファイルを行単位でN分割して別のファイルに格納せよ
N=10

filename="mao/chapter02/popular-names.txt"
with open(filename,"r") as f:
    for i in range(N):
        line=f.readline()
        with open(f"knock15_split_{i}.txt","w") as out_file:
            out_file.write(line)

#UNIXコマンド
#split -l 分割後の行数　ファイル名　プレフィックス(新しいファイル名の先頭につく文字)
#head -n 10 mao/chapter02/popular-names.txt | split -l 1 -d - output_