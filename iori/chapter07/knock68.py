import pandas as pd
from knock62 import model, vectorizer

feature_names = vectorizer.get_feature_names_out()
coefficients = model.coef_[0]

coef_df = pd.DataFrame({
    'Feature': feature_names,
    'Coefficient': coefficients
})

top_positive = coef_df.nlargest(20, 'Coefficient')
top_negative = coef_df.nsmallest(20, 'Coefficient')

print("Top 20 positive features:")
print(top_positive)

print("\nTop 20 negative features:")
print(top_negative)

'''
Top 20 positive features:
           Feature  Coefficient
10593   refreshing     3.437025
10675   remarkable     3.434638
9915      powerful     3.224946
6169     hilarious     3.185373
1263     beautiful     3.004350
14622    wonderful     2.974466
10145        prose     2.920007
13103     terrific     2.878946
788      appealing     2.858988
4321     enjoyable     2.818534
13492        treat     2.809406
2180       charmer     2.755490
14212      vividly     2.716752
7627       likable     2.694100
12089        solid     2.655623
4802   fascinating     2.621313
2181      charming     2.620602
5877      half-bad     2.611829
6574    impressive     2.599161
6901    intriguing     2.564417

Top 20 negative features:
             Feature  Coefficient
7365         lacking    -4.339461
7367           lacks    -4.082975
14674          worst    -3.984160
3543          devoid    -3.659673
8216            mess    -3.628446
4729         failure    -3.587995
12618         stupid    -3.351428
1615            bore    -3.261353
5021            flat    -3.226835
3456      depressing    -3.204095
7780           loses    -3.177648
14322          waste    -3.159570
7361            lack    -3.062670
12321      squanders    -3.036976
5973          hardly    -3.028998
8844            none    -3.021222
9829            poor    -2.987390
9789       pointless    -2.966517
13856  unfortunately    -2.946167
7793           lousy    -2.942092
'''