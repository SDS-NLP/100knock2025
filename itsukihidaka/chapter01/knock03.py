# “Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.”という文を単語に分解し、各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ。

text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

word_list = text.split()

word_length_list = [len(word.rstrip(".,")) for word in word_list]

print(word_length_list)