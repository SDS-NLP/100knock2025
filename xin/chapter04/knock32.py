from janome.tokenizer import Tokenizer
import knock30

text=knock30.text

# 形態素解析器の初期化
tokenizer = Tokenizer()

# 文章を解析
tokens = list(tokenizer.tokenize(text))

# 「名詞 の 名詞」のパターンを抽出
noun_phrases = []
for i in range(len(tokens) - 2):
    if "名詞" in tokens[i].part_of_speech and tokens[i+1].surface == "の" and "名詞" in tokens[i+2].part_of_speech:
        noun_phrases.append(tokens[i].surface + "の" + tokens[i+2].surface)

# 結果の表示
print(noun_phrases)