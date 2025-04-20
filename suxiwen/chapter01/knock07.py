def generate_sentence(x, y, z):
    return f"{x}時の{y}は{z}"

# 実行結果の確認
result = generate_sentence(12, "気温", 22.4)
print(result)