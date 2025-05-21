# 分からん
import json
import gzip
import re
import subprocess
import os
from collections import Counter


def remove_markup(text):
    # 強調マークアップの除去
    text = re.sub(r"\'{2,5}", "", text)
    # 内部リンクの除去
    text = re.sub(r"\[\[(?:[^|\]]*?\|)??([^|\]]+?)\]\]", r"\1", text)
    # 外部リンクの除去
    text = re.sub(r"\[http://[^\]]+\]", "", text)
    # HTMLタグの除去
    text = re.sub(r"<[^>]+>", "", text)
    # テンプレートの除去
    text = re.sub(r"\{\{.*?\}\}", "", text)
    return text


def analyze_word_frequency():
    # 形態素解析にmecab CLIを使用 (mecab と -Owakati オプションが必要)
    # Python MeCabバインディングを避ける

    # 単語の出現頻度をカウントするためのCounter
    word_counter = Counter()

    # gzipファイルを読み込む
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_gz_path = os.path.join(script_dir, "jawiki-country.json.gz")
    with gzip.open(json_gz_path, "rt", encoding="utf-8") as f:
        for line in f:
            article = json.loads(line)
            text = article["text"]

            # マークアップを除去
            text = remove_markup(text)

            # 形態素解析を行い、単語をカウント
            result = subprocess.run(["mecab", "-Owakati"], input=text, text=True, capture_output=True)
            words = result.stdout.strip().split()
            word_counter.update(words)

    # 出現頻度の高い20語を表示
    for word, count in word_counter.most_common(20):
        print(f"{word}: {count}")


def load_cleaned_articles():
    """
    Load and clean wiki country articles from JSON gz file.
    Returns list of dicts with 'title' and 'text' keys.
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    json_gz_path = os.path.join(script_dir, "jawiki-country.json.gz")
    cleaned_articles = []
    with gzip.open(json_gz_path, "rt", encoding="utf-8") as f:
        for line in f:
            article = json.loads(line)
            text = remove_markup(article["text"])
            cleaned_articles.append({"title": article.get("title", ""), "text": text})
    return cleaned_articles


if __name__ == "__main__":
    analyze_word_frequency()