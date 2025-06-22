"""
knock61：特徴ベクトル
Bag of Words (BoW) に基づき、学習データ（train.tsv）および検証データ（dev.tsv）
のテキストを特徴ベクトルに変換したい。

ここで、ある事例のテキストの特徴ベクトルは、テキスト中に含まれる単語（スペース区切りのトークン）の出現頻度で構成する。
例えば、”too loud , too goofy”というテキストに対応する特徴ベクトルは、
以下のような辞書オブジェクトで表現される。
{'too': 2, 'loud': 1, ',': 1, 'goofy': 1}

各事例はテキスト、特徴ベクトル、ラベルを格納した辞書オブジェクトでまとめておく。
例えば、先ほどの”too loud , too goofy”に対してラベル”0”（ネガティブ）が付与された事例は、
以下のオブジェクトで表現される。
{'text': 'too loud , too goofy', 'label': '0', 'feature': {'too': 2, 'loud': 1, ',': 1, 'goofy': 1}}

学習データと検証データの各事例を上記のような辞書オブジェクトに変換したうえで、
学習データと検証データのそれぞれを、辞書オブジェクトのリストとして表現せよ。
さらに、学習データの最初の事例について、正しく特徴ベクトルに変換できたか、目視で確認せよ。
"""
import pandas as pd
from collections import Counter

#データの読み込み
df_train=pd.read_csv("mao/chapter07/SST-2/train.tsv",sep='\t')
df_dev=pd.read_csv("mao/chapter07/SST-2/dev.tsv",sep='\t')

#特徴ベクトルへの変換関数
def convert_to_bow_dataset(df):
    dataset = []
    for _, row in df.iterrows():
        text = row['sentence']
        label = str(row['label'])       #ラベルを文字列に変換（指定どおり）
        tokens = text.split()           #スペース区切りでトークン化
        feature = dict(Counter(tokens)) #BoW特徴ベクトル
        entry = {
            'text': text,
            'label': label,
            'feature': feature
        }
        dataset.append(entry)
    return dataset

#BoW変換
train_bow=convert_to_bow_dataset(df_train)
dev_bow=convert_to_bow_dataset(df_dev)
if __name__=="__main__":
    #学習データの最初の事例を確認
    print("🔎 学習データの最初の事例：")
    print(train_bow[0])
