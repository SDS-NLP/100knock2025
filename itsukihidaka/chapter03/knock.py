# Wikipedia記事のJSONファイルを読み込み、「イギリス」に関する記事本文を表示せよ。問題21-29では、ここで抽出した記事本文に対して実行せよ。

import json

def read_wiki_data():
    file_path = '/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter03/jawiki-country.json'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data = json.loads(line)
            if data['title'] == 'イギリス':
                return data['text']
    
    return None

uk_text = read_wiki_data()
if uk_text:
    print(uk_text)
else:
    print('イギリスの記事が見つかりませんでした。')

# 抽出したイギリスの記事をファイルに出力する
output_file_path = '/Users/itsukihidaka/Desktop/基礎勉強会/100knock2025/itsukihidaka/chapter03/uk_article.txt'

if uk_text:
    with open(output_file_path, 'w', encoding='utf-8') as f:
        f.write(uk_text)
    print(f'イギリスの記事を {output_file_path} に出力しました。')
else:
    print('イギリスの記事が見つからなかったため、ファイル出力できませんでした。')
