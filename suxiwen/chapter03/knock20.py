import gzip
import json

def extract_uk_text(file_path):
    with gzip.open(file_path, "rt", encoding="utf-8") as f:
        for line in f:
            data = json.loads(line.strip())
            if data["title"] == "イギリス":
                return data["text"]
    return "『イギリス』の記事が見つかりません"

uk_text = extract_uk_text("jawiki-country.json.gz")
print(uk_text)
    