sentence = ("Hi He Lied Because Boron Could Not Oxidize Fluorine."
            "New Nations Might Also Sign Peace Security Clause. Arthur King Can.")

special_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}

words = sentence.replace(".", "").split()

result = { (word[:1] if i in special_positions else word[:2]) : i
           for i, word in enumerate(words, 1) }

print(result)
