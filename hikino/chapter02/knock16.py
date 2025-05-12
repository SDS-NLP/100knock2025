import pandas as pd
df = pd.read_csv("../../../popular-names.txt", sep="\t", header = None)
print(df.sample(frac=1))

#shuf ../../../popular-names.txt | head -n 10
#実行結果
# Sophia  F       20643   2010
# Carol   F       20166   1939
# Barbara F       30696   1935
# James   M       39371   1979
# Henry   M       2383    1883
# Justin  M       30641   1990
# Thomas  M       43778   1948
# Emma    F       2698    1897
# Shirley F       17878   1940
# Margaret        F       1821    1882