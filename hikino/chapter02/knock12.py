import pandas as pd
df = pd.read_csv("../../../popular-names.txt", header = None)
print(df.tail(10))

#tail ../../../popular-names.txt
#実行結果
# Liam    M       19837   2018
# Noah    M       18267   2018
# William M       14516   2018
# James   M       13525   2018
# Oliver  M       13389   2018
# Benjamin        M       13381   2018
# Elijah  M       12886   2018
# Lucas   M       12585   2018
# Mason   M       12435   2018
# Logan   M       12352   2018