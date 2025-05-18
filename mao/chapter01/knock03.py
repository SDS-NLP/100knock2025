text="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words=text.split() #単語に分割
counts=[]

for word in words:
    word=word.strip(",.") #アルファベット以外の文字を消去
    counts.append(len(word))

#結果表示
print(counts)
