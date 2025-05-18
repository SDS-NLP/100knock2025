import pandas as pd

df = pd.read_table('iori/chapter02/popular-names.txt', header=None)

print(set(df.iloc[:,0]))

#cut -f 1 iori/chapter02/popular-names.txt | sort | uniq

'''Abigail
Aiden
Alexander
Alexis
Alice
Amanda
Amelia
Amy
Andrew
Angela
Anna'''