#37. 名詞の出現頻度
import spacy
from collections import Counter

# GiNZAの日本語モデルを読み込む
nlp = spacy.load("ja_ginza")

# 出現頻度をカウントするCounterオブジェクト
noun_freq = Counter()

# テキストファイルの読み込み
with open("kokoro.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        try:
            doc = nlp(line)
            for token in doc:
                # 名詞だけ抽出（固有名詞・普通名詞なども含む）
                if token.pos_ == "NOUN" or token.pos_ == "PROPN":
                    noun_freq[token.lemma_] += 1
        except Exception as e:
            print(f"Error: {e} for line: {line[:30]}...")

# 出現頻度の高い名詞20語を表示
print("出現頻度の高い名詞トップ20：")
for word, count in noun_freq.most_common(20):
    print(f"{word}\t{count}")
