def n_gram(sequence, n):
    """与えられたシーケンスから n-gram を生成する関数"""
    return [sequence[i:i+n] for i in range(len(sequence) - n + 1)]

# 文字 tri-gram の生成
text = "I am an NLPer"
char_tri_gram = n_gram(text.replace(" ", ""), 3)  # 空白を除去して文字単位で分割

# 単語 bi-gram の生成
words = text.split()
word_bi_gram = n_gram(words, 2)  # 単語単位で分割

# 結果を表示
print("文字 tri-gram:", char_tri_gram)
print("単語 bi-gram:", word_bi_gram)
