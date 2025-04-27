import pandas as pd

with open("../../../popular-names.txt", "r") as f:
    lines = f.readlines()
    count = len(lines)
    print(count)

df = pd.read_csv("../../../popular-names.txt", header = None)
print(len(df))

#wc -l ../../../popular-names.txt
#実行結果 2780