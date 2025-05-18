def cipher(text):
    result = ''
    for char in text:
        if char.islower():
            # 小文字なら (219 - 文字コード)
            result += chr(219 - ord(char))
        else:
            # その他の文字はそのまま
            result += char
    return result

# 元のメッセージ
original = "I love Natural Language Processing 101!"

# 暗号化
encrypted = cipher(original)
print("暗号化:", encrypted)

# 復号化（再度cipher関数を適用）
decrypted = cipher(encrypted)
print("復号化:", decrypted)
