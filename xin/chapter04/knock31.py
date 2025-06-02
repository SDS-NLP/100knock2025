import knock30
from janome.tokenizer import Tokenizer
from janome.tokenizer import Tokenizer


text=knock30.text

# 形態素解析器の初期化
tokenizer = Tokenizer()

# 文章を解析
tokens = tokenizer.tokenize(text)

# 動詞を抽出（表層形と基本形のペア）
verbs = []
for token in tokens:
    part = token.part_of_speech.split(',')[0]
    if part == "動詞":
        verbs.append((token.surface, token.base_form))

# 結果の表示
for verb, base_form in verbs:
    print(f'{verb}:{base_form}')
