#60. データの入手・整形

positive_train=0
negative_train=0
unknown_train=0
with open("SST-2/train.tsv", "r") as f:
    for line in f:
        line=line.strip().split("\t")
        if line[1] == "1":
            positive_train += 1
        elif line[1] == "0":
            negative_train += 1
        else:
            continue
            unknown_train += 1
            print(line,"データがありません") #最初の行だけ

print("訓練データ")
print("ポジティブ：", positive_train, "件")
print("ネガティブ：", negative_train, "件")

positive_dev=0
negative_dev=0
unknown_dev=0
with open("SST-2/dev.tsv", "r") as f:
    for line in f:
        line=line.strip().split("\t")
        if line[1] == "1":
            positive_dev += 1
        elif line[1] == "0":
            negative_dev += 1
        else:
            continue
            unknown_dev += 1
            print(line,"データがありません") #最初の行だけ

print("検証データ")
print("ポジティブ：", positive_dev, "件")
print("ネガティブ：", negative_dev, "件")

