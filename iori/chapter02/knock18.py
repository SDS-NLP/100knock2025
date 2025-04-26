import pandas as pd

df = pd.read_table('iori/chapter02/popular-names.txt', header=None)

print(df[0].value_counts())

#cut -f 1 iori/chapter02/popular-names.txt | sort | uniq -c | sort -nr

'''118 James
 111 William
 108 Robert
 108 John
  92 Mary
  75 Charles
  74 Michael
  73 Elizabeth
  70 Joseph
  60 Margaret'''