# $ brew install mecab
# $ brew install mecab-ipadic
# $ pip install mecab-python3
# $ python -m pip install mecab ← ここで苦戦した！

import os
text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "melos.mecab")

# 形態素解析
if __name__ == "__main__":
    import MeCab # 日本語向け形態素解析ツール

    mecab = MeCab.Tagger("-r/opt/homebrew/etc/mecabrc")
    result = mecab.parse(text)
    with open(file_path, "w") as f:
        f.write(result)
    print(result)

# 形態素解析結果の読み込み
with open(file_path, "r") as f:
  general_list = []
  melos_list = []
  lines = f.readlines()
  for line in lines:
    melos_dic = {}
    suf = line.split("\t")
    if suf[0] == "EOS\n":
      continue
    temp = suf[1].split(',')
    melos_dic["surface"] = suf[0] #表層形
    if len(temp) <= 7:
      melos_dic["base"] = suf[0] #基本形
    else:
      melos_dic["base"] = temp[7]
    melos_dic["pos"] = temp[0] #品詞
    melos_dic["pos1"] = temp[1] #品詞細分類1
    melos_list.append(melos_dic)
    if suf[0]=="。":
      general_list.append(melos_list)
      melos_list = []