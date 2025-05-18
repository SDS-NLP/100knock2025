def cipher(text: str) -> str:
    result = []
    for char in text:
        if 'a' <= char <= 'z':
            result.append(chr(219 - ord(char)))
        else:
            result.append(char)
    return "".join(result)

message: str = "All you need is security! 1, 2, 3. あ、い、う。"

encrypted_message = cipher(message)
print(f"原文　: {message}")
print(f"暗号文: {encrypted_message}")

decrypted_message = cipher(encrypted_message)
print(f"復号文: {decrypted_message}")