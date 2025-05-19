import gzip
import json
import re
import MeCab
import os
from collections import Counter

def clean_markup(text):
    text = re.sub(r"'{2,5}", "", text)
    text = re.sub(r"\[\[.*?\|(.*?)\]\]", r"\1", text)
    text = re.sub(r"\[\[.*?#.*?\|(.*?)\]\]", r"\1", text)
    text = re.sub(r"\[\[(.*?#.*?)\]\]", lambda m: m.group(1).split('#')[0], text)
    text = re.sub(r"\[\[(.*?)\]\]", r"\1", text)
    text = re.sub(r"\{\{lang\|[^\|]+\|([^\}]+)\}\}", r"\1", text)
    text = re.sub(r"\{\{仮リンク\|([^\|]+)\|[^}]+\}\}", r"\1", text)
    text = re.sub(r"\{\{.*?\}\}", "", text)
    return text

def load_cleaned_articles(filepath="jawiki-country.json.gz"):
    articles = []
    with gzip.open(filepath, "rt", encoding="utf-8") as f:
        for line in f:
            article = json.loads(line)
            text = clean_markup(article.get("text", ""))
            articles.append({
                "title": article.get("title", ""),
                "text": text
            })
    return articles

def get_all_tokens(articles):
    unidic_path = os.path.expanduser("~/unidic-cwj")
    mecabrc_path = "/etc/mecabrc"

    mecab = MeCab.Tagger(
        f"-r {mecabrc_path} -d {unidic_path} "
        "-F '\\t%m\\t%f[7]\\t%f[6]\\t%f[23]\\t%F-[0,1,2,3]\\t%f[4]\\t%f[5]\\t%f[8]\\t%f[9]\\t%f[12]\\t%f[28]\\n' "
        "--unk-format='\\t%m\\t\\t\\t未知語\\t\\t\\n'"
    )
    mecab.parse("")  # 初期化バグ対策

    tokens = []
    for article in articles:
        parsed = mecab.parse(article["text"])
        lines = parsed.strip().split("\n")

        for line in lines:
            if not line.strip() or line.startswith("EOS") or line.startswith("B"):
                continue

            parts = line.split()
            if len(parts) >= 5:
                surface = parts[0]
                lemma = parts[1]
                pos = parts[4]

                if "補助記号" in pos or "記号" in pos:
                    continue

                tokens.append(lemma)  # 原形を使ってカウント
    return tokens

if __name__ == "__main__":
    articles = load_cleaned_articles()

#    print("🧹 クリーニング後の本文サンプル（3記事分）:")
#    for i, article in enumerate(articles[:3]):  # 先頭3件だけ確認
#        print(f"\n--- [{i+1}] {article['title']} ---")
#        lines = article['text'].strip().split("\n")
#        for line in lines[:5]:  # 各記事の冒頭5行を表示
#            print(line)
#        print("...")

    words = get_all_tokens(articles)
    counter = Counter(words)

    print("📊 出現頻度上位20語（補助記号除外）:")
    for word, freq in counter.most_common(50):
        print(f"{word}\t{freq}")