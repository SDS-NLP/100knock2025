sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
words = sentence.split()
special = {1,5,6,7,8,9,15,16,19}
element_dict = {
    i+1: word.rstrip('.')[0] if (i+1) in special else word.rstrip('.')[:2]
    for i, word in enumerate(words)
}
print(element_dict)