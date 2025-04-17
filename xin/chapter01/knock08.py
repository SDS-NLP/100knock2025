def cipher(text):
    """英小文字を (219 - 文字コード) に対応する文字へ変換する暗号化・復号化関数"""
    return "".join(chr(219 - ord(c)) if c.islower() else c for c in text)

# 実行例
message = "Hello, World!"
encrypted_message = cipher(message)
decrypted_message = cipher(encrypted_message)

# 結果表示
print("Original:", message)
print("Encrypted:", encrypted_message)
print("Decrypted:", decrypted_message)