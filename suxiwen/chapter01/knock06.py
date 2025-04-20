# 一行でbi-gram生成と集合演算をまとめる
str_x, str_y = "paraparaparadise", "paragraph"
X, Y = ({str_x[i:i+2] for i in range(len(str_x)-1)},  # Xのbi-gram集合
        {str_y[i:i+2] for i in range(len(str_y)-1)})  # Yのbi-gram集合

# 結果出力（直接演算結果を表示）
print("和集合:", X | Y)
print("積集合:", X & Y)
print("差集合:", X - Y)
print("'se'がXに含まれる？", 'se' in X)  # True
print("'se'がYに含まれる？", 'se' in Y)  # False