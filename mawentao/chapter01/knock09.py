#!/usr/bin/env python
# coding: utf-8

# In[77]:


#09. Typoglycemia
str1 = 'I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind .'

import random

def letter_count(word):
    return sum(c.isalpha() for c in word)

def shuffle(word):
    if letter_count(word) <= 4:
        return word

    first = word[0]
    last = word[-1]
    middle = list(word[1:-1])

    random.shuffle(middle)
    return first + ''.join(middle) + last

words = str1.split()
shuffled_words = [shuffle(word) for word in words]
result = ' '.join(shuffled_words)

print(result)




