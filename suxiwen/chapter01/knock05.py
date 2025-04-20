def create_ngram(sequence, n):
    """
    シーケンスからn-gramを生成する関数
    :param sequence: 文字列またはリストのシーケンス
    :param n: n-gramのn値（例：3→tri-gram, 2→bi-gram）
    :return: n-gramのリスト（タプルで格納）
    """
    return [tuple(sequence[i:i+n]) for i in range(len(sequence) - n + 1)]

# 入力文
sentence = "I am an NLPer"

# 文字tri-gram（文字列を1文字ずつのリストに変換）
char_sequence = list(sentence)  # 文字のリスト: ['I', ' ', 'a', 'm', ' ', 'a', 'n', ' ', 'N', 'L', 'P', 'e', 'r']
char_trigram = create_ngram(char_sequence, 3)

# 単語bi-gram（文字列をスペースで分割したリスト）
word_sequence = sentence.split()  # 単語のリスト: ['I', 'am', 'an', 'NLPer']
word_bigram = create_ngram(word_sequence, 2)

# 結果出力
print("文字tri-gram：", char_trigram)
print("単語bi-gram：", word_bigram)