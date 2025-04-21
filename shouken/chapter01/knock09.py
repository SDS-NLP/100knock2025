import random
text = "I couldn’t believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
text = text.replace(".", "")
words = text.split(" ")
result_words = []

for word in words:
    if len(word) <= 4:
        result_words.append(word)
    else:
      head = word[0]
      tail = word[-1]
      middle = list(word[1:-1])
      random.shuffle(middle)
      shuffled = head + ''.join(middle) + tail
      result_words.append(shuffled)

final_result = ' '.join(result_words) + "."
print(final_result)
