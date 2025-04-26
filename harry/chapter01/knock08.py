def cipher(text):
    result = ''
    for c in text:
        if c.islower():
            result += chr(219 - ord(c))
        else:
            result += c
    return result

# 入力を受け取る
original = input("元の文を入力してください： ")

# 暗号化
encrypted = cipher(original)
# 復号化（もう一度cipherを使う）
decrypted = cipher(encrypted)

# 結果表示
print("暗号化された文：", encrypted)
print("復号化された文：", decrypted)
