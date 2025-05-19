# $ brew install mecab
# $ brew install mecab-ipadic
# $ brew install mecab-unidic
# $ pip install mecab-python3
# $ python -m pip install mecab ← ここで苦戦した！

import MeCab
import unidic
import os

# パスの特定
script_dir = os.path.dirname(os.path.abspath(__file__))
input_path = os.path.join(script_dir, "kokoro.txt")
output_path = os.path.join(script_dir, "kokoro.mecab")

# Initialize MeCab with the correct configuration file path
mecab = MeCab.Tagger("-r/opt/homebrew/etc/mecabrc")
# Use the actual path to kokoro.txt in the same directory
with open(input_path, "r") as f, open(output_path, "w") as f2:
    lines = f.readlines()
    for text in lines:
        result = mecab.parse(text)
        f2.write(result)