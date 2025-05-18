import pandas as pd

df = pd.read_table('iori/chapter02/popular-names.txt', header=None)

print(df.sort_values(2, ascending=False))

#sort -k 3,3nr iori/chapter02/popular-names.txt

'''Alice   F       1542    1882
Bertha  F       1508    1882
Annie   F       1492    1882
Ida     F       1472    1880
Ida     F       1439    1881
Alice   F       1414    1880
Annie   F       1326    1881
Bertha  F       1324    1881
Bertha  F       1320    1880
Alice   F       1308    1881
Sarah   F       1288    1880ß'''