from knock36 import clean_text
import gzip
import json
import re
from collections import Counter
import MeCab
from tqdm import tqdm
noun_counter = Counter()
tagger= MeCab.Tagger()
with gzip.open('/home/tanxin/100knock2025/xin/chapter03/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in tqdm(f):
        article = json.loads(line)
        text = clean_text(article.get('text', ''))
        parsed = tagger.parse(text)
        for line in parsed.splitlines():
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            surface = parts[0]
            features = parts[4].split('-')
            if features[0]=='名詞' and features[1] not in {'非自立', '接尾','数詞'}:
               noun_counter[surface] += 1

# 出現頻度上位20名詞を表示
for word, count in noun_counter.most_common(20):
    print(f'{word}: {count}')

