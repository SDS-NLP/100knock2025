from collections import Counter
from knock36 import load_cleaned_articles
import MeCab
import os

def get_tokens_by_pos(articles, target_pos_prefix="名詞"):
    """
    指定した品詞（例："名詞"）の原形のみを抽出して返す
    補助記号や記号は除外
    """
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

                if (
                    target_pos_prefix in pos and
                    "補助記号" not in pos and
                    "記号" not in pos
                ):
                    tokens.append(lemma)  # 原形を使ってカウント
    return tokens

if __name__ == "__main__":
    articles = load_cleaned_articles()
    words = get_tokens_by_pos(articles, target_pos_prefix="名詞-普通名詞")
    counter = Counter(words)

    print("🔢 名詞（普通名詞）の出現頻度 上位20語：")
    for word, freq in counter.most_common(20):
        print(f"{word}\t{freq}")