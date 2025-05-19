import math
from collections import Counter
from knock36 import load_cleaned_articles
from knock37 import get_tokens_by_pos

# 1. 全記事を読み込み
articles = load_cleaned_articles()
total_docs = len(articles)

# 2. 各記事から名詞リストを抽出
article_nouns_list = [set(get_tokens_by_pos([article], target_pos_prefix="名詞")) for article in articles]

# 3. 「日本」記事の名詞を抽出（TF対象）
japan_article = next((a for a in articles if a["title"] == "日本"), None)
if not japan_article:
    raise ValueError("『日本』の記事が見つかりませんでした。")

japan_nouns = get_tokens_by_pos([japan_article], target_pos_prefix="名詞")
tf_counter = Counter(japan_nouns)

# 4. IDFを計算：各語が何文書に出現するか
df_counter = Counter()
for noun_set in article_nouns_list:
    for word in noun_set:
        df_counter[word] += 1

# 5. TF-IDFスコアを計算
tf_idf_scores = []
for word, tf in tf_counter.items():
    df = df_counter.get(word, 1)  # 出現しない語がいないとは限らない
    idf = math.log(total_docs / df)
    tf_idf = tf * idf
    tf_idf_scores.append((word, tf, round(idf, 4), round(tf_idf, 4)))

# 6. スコアの高い順にソート
tf_idf_scores.sort(key=lambda x: x[3], reverse=True)

# 7. 上位20語を表示
print("🧠 日本記事における名詞のTF-IDF上位20語")
print(f"{'語':<10}\t{'TF':<5}\t{'IDF':<8}\t{'TF-IDF'}")
for word, tf, idf, tf_idf in tf_idf_scores[:20]:
    print(f"{word:<10}\t{tf:<5}\t{idf:<8}\t{tf_idf}")