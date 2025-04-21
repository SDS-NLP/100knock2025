text = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
text = text.replace(".", "")
words = text.split()
hitomojidake = [1, 5, 6, 7, 8, 9, 15, 16, 19]
result = {}

for index, word in enumerate(words, start=1):
    if index in hitomojidake:
        result[index] = word[:1]
    else:
        result[index] = word[:2]


for k in sorted(result.keys()):
    print(f"{k}: {result[k]}")
    