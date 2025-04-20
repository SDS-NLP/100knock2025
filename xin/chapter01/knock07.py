def format_sentence(x, y, z):
    """引数 x, y, z を受け取り、指定の形式で文字列を返す"""
    return f"{x}時の{y}は{z}"

# 実行例
x = 12
y = "気温"
z = 22.4

result = format_sentence(x, y, z)
print(result)