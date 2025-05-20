import gzip, json, re, math
from collections import Counter, defaultdict
import MeCab
from tqdm import tqdm
from knock36 import clean_text
noun_counter = Counter()
docs_tf = []
df = Counter()
doc_count = 0
tagger= MeCab.Tagger()
with gzip.open('/home/tanxin/100knock2025/xin/chapter03/jawiki-country.json.gz', 'rt', encoding='utf-8') as f:
    for line in tqdm(f):
        article = json.loads(line)
        title = article.get('title', '')
        if '日本'not in title:
            continue
        text = clean_text(article.get('text', ''))
        parsed = tagger.parse(text)
        words_in_doc = set()
        tf=Counter()
        for line in parsed.splitlines():
            parts = line.split('\t')
            if len(parts) < 2:
                continue
            surface = parts[0]
            features = parts[4].split('-')
            if features[0]=='名詞' and features[1] not in {'非自立', '接尾','数詞'}:
               noun_counter[surface] += 1
               tf[surface] += 1
               words_in_doc.add(surface)
        docs_tf.append(tf)

        # 文書ごとの名詞出現頻度をカウント (DF)
        for word in words_in_doc:
            df[word] += 1
        
        doc_count += 1

            


def tfidf(tf, df, N):
    return tf * math.log(N/df+1) if df>0 else 0.0

# 単語ごとに最大TF-IDFを計算
word_tfidf = {}
for w in df:
    max_score = 0
    for tf in docs_tf:
        if tf[w]>0:
            score = tfidf(tf[w], df[w], doc_count)
            if score>max_score:
                max_score = score
    word_tfidf[w] = max_score

# 上位20語
top20 = sorted(word_tfidf.items(), key=lambda x: x[1], reverse=True)[:20]

print(f'{"単語":<15}{"TF":>5}{"DF":>5}{"TF-IDF":>10}')
for w, sc in top20:
    # 最大TFを再取得
    max_tf = max(tf[w] for tf in docs_tf)
    print(f'{w:<15}{max_tf:>5}{df[w]:>5}{sc:>10.4f}')
