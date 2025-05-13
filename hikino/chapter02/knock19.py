import pandas as pd

df = pd.read_csv("../../../popular-names.txt", sep="\t", header=None)
df_sort = df.sort_values([2], ascending=False)
print(df_sort.head(10))

#sort -r ../../../popular-names.txt | head -n 10
#実行結果
# William M       9532    1880
# William M       9298    1882
# William M       8897    1884
# William M       8844    1910
# William M       8705    1888
# William M       8579    1900
# William M       8524    1881
# William M       8387    1883
# William M       8252    1886
# William M       8044    1885