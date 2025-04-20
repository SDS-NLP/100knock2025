def cipher(text):
    return "".join(chr(219 - ord(c)) if c.islower() else c for c in text)
message = "Hello World"
ango_message = cipher(message)
fukugo_message = cipher(ango_message)
print("元のメッセージ:", message)
print("暗号化されたメッセージ:", ango_message)
print("複合化されたメッセージ:", fukugo_message)