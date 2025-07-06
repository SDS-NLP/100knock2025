"""
knock60:データの入手・整形
GLUEのウェブサイトからSST-2データセットを取得せよ。
学習データ（train.tsv）と検証データ（dev.tsv）のぞれぞれについて、
ポジティブ (1) とネガティブ (0) の事例数をカウントせよ。
"""
import pandas as pd

df_train = pd.read_csv("mao/chapter07/SST-2/train.tsv", sep='\t')
df_dev = pd.read_csv("mao/chapter07/SST-2/dev.tsv", sep='\t')

#print(df_train.head())
print("Trainデータのラベル数")
print(df_train['label'].value_counts())
print("Devデータのラベル数")
print(df_dev['label'].value_counts())