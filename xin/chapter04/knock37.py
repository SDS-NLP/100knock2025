from knock36 import clean_text
import gzip
import json
import re
from collections import Counter
import MeCab
from tqdm import tqdm
#コーパスにおける名詞の出現頻度を求め、出現頻度の高い20語とその出現頻度を表示せよ。
#名詞の頻度を記録するためのカウンターを作成
noun_counter = Counter()
# MeCabの初期化
tagger= MeCab.Tagger()
with gzip.open('/home/tanxin/100knock2025/xin/chapter03/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in tqdm(f):
        article = json.loads(line)
        text = clean_text(article.get('text', ''))
        parsed = tagger.parse(text) #東京    トーキョー      トウキョウ      トウキョウ      名詞-固有名詞-地名-一般                 0
        for line in parsed.splitlines():
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            if parts[0]==parts[1]==parts[2]==parts[3]:
                continue         #a       a       a       a       名詞-普通名詞-一般                      0
            surface = parts[0]
            features = parts[4].split('-')
            if features[0]=='名詞' and features[1] not in {'非自立', '接尾','数詞'}:
               noun_counter[surface] += 1

# 出現頻度上位20名詞を表示
for word, count in noun_counter.most_common(20):
    print(f'{word}: {count}')

