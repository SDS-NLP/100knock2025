import MeCab
import ipadic

text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

tagger = MeCab.Tagger(ipadic.MECAB_ARGS)
parsed_text = tagger.parse(text)

noun_phrases = []
lines = parsed_text.split("\n")
for i in range(len(lines) - 2):  
    if lines[i] == "" or lines[i + 1] == "" or lines[i + 2] == "":
        continue
    word1, word2, word3 = lines[i].split("\t"), lines[i + 1].split("\t"), lines[i + 2].split("\t")
    if len(word1) > 1 and len(word2) > 1 and len(word3) > 1:
        if word1[1].startswith("名詞") and word2[0] == "の" and word3[1].startswith("名詞"):
            noun_phrases.append(word1[0] + word2[0] + word3[0])

print(noun_phrases)