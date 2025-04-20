sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = sentence.split()  
letter_counts = [len(word.rstrip(',.')) for word in words]  
print(letter_counts)