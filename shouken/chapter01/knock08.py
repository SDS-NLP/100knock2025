def angou(text):
    result = ""
    for a in text:
        if a.islower():
            result = result + chr(219 - ord(a))
        else:
            result = result + a
    return result

text = "Now I need a drink."
encrypted = angou(text)
print("暗号化：", encrypted)

print("復号化：", angou(encrypted))