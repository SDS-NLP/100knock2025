import gzip
import json

input_file = 'jawiki-country.json.gz'
output_file = 'uk_article.json'

uk_article = None

with gzip.open(input_file, 'rt', encoding='utf-8') as f:
    for line in f:
        data = json.loads(line)
        if data['title'] == 'イギリス':
            uk_article = data  # title, text を含む全体を保存
            break

if uk_article:
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(uk_article, f, ensure_ascii=False, indent=2)
    print(f"✅ イギリスの記事を JSON 形式で「{output_file}」に保存しました。")
else:
    print("❌ 「イギリス」の記事が見つかりませんでした。")
