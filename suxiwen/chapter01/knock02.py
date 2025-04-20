import re


sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

words = sentence.split()

def count_letters(word):
    cleaned_word = re.sub(r'[^a-zA-Z]', '', word) 
    return len(cleaned_word)


letter_counts = [count_letters(word) for word in words]

print(letter_counts)  