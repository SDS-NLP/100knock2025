#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import MeCab
with open('/Users/niaomuqing/100knock2025/走れメロス.txt', 'r', encoding='utf-8') as f:
    text = f.read()

mecab = MeCab.Tagger('-r /opt/homebrew/etc/mecabrc')
parsed = mecab.parse(text)

#結果をリストに格納する
lines = [line for line in parsed.splitlines() if line != 'EOS' and line.strip()]

# print(lines)
# 'メロス\t名詞,一般,*,*,*,*,*'　「\t」が入っている

tokens = []
for line in lines:
    surface, feature_str = line.split('\t')
    features = feature_str.split(',')
    tokens.append({'surface': surface, 'pos': features[0], 'pos1':features[1] })

# 「名詞 の 名詞」
for i in range(1, len(tokens) - 1):
    if (tokens[i]['surface'] == 'の' and
        tokens[i]['pos'] == '助詞' and
        # tokens[i]['pos1'] == '格助詞' and
        tokens[i-1]['pos'] == '名詞' and
        tokens[i+1]['pos'] == '名詞'):
        phrase = tokens[i-1]['surface'] + 'の' + tokens[i+1]['surface']
        print(phrase)

# # # 「の」の品詞を確認する。
# # for i in range(1, len(tokens) - 1):
# #     if tokens[i]['surface'] == 'の':
# #         print(f"\n【の】→ {tokens[i]}")


# In[ ]:




