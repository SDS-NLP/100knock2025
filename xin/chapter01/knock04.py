sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = [word.strip(".") for word in sentence.split()]
one_letter_positions = {1, 5, 6, 7, 8, 9, 15, 16, 19}
word_map = {i+1: (word[0] if i+1 in one_letter_positions else word[:2]) for i, word in enumerate(words)}
print(word_map)