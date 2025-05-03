import pandas as pd
df = pd.read_csv("../../../popular-names.txt", sep="\t", header = None)
df_lst = df[0].to_list()
df_set = set(df_lst)
print(len(df_set))

#cut -f 1 ../../../popular-names.txt | sort | uniq |wc -l
#実行結果
#136