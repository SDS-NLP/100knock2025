"""
knock71:データセットの読み込み
General Language Understanding Evaluation (GLUE) ベンチマークで
配布されているStanford Sentiment Treebank (SST) をダウンロードし、
訓練セット（train.tsv）と開発セット（dev.tsv）のテキストと極性ラベルを
読み込み、全てのテキストをトークンID列に変換せよ。

このとき、単語埋め込みの語彙でカバーされていない単語は無視し、
トークン列に含めないことにせよ。
また、テキストの全トークンが単語埋め込みの語彙に含まれておらず、
空のトークン列となってしまう事例は、訓練セットおよび開発セットから削除せよ
（このため、第7章の実験で得られた正解率と比較できなくなることに注意せよ）。

事例の表現方法は任意でよいが、
例えば”contains no wit , only labored gags”がネガティブに分類される
事例は、次のような辞書オブジェクトで表現すればよい。

{'text': 'contains no wit , only labored gags',
 'label': tensor([0.]),
 'input_ids': tensor([ 3475,    87, 15888,    90, 27695, 42637])}

この例では、textはテキスト、labelは分類ラベル
（ポジティブならtensor([1.])、ネガティブならtensor([0.])）、
input_idsはテキストのトークン列をID列で表現している。
"""
import csv
import torch
from tqdm import tqdm  # ← 追加
from knock70 import word2id

def load_sst_dataset(filepath, word2id):
    dataset = []
    with open(filepath, encoding='utf-8') as f:
        reader = list(csv.DictReader(f, delimiter='\t'))  # ← 一度 list 化する
        total = len(reader)
        skipped = 0

        for row in tqdm(reader, desc=f'Loading {filepath}', total=total):  # ← tqdmで包む
            text = row['sentence']
            label = torch.tensor([float(row['label'])])

            tokens = text.lower().split()
            input_ids = [word2id[word] for word in tokens if word in word2id]

            if len(input_ids) == 0:
                skipped += 1
                continue

            dataset.append({
                'text': text,
                'label': label,
                'input_ids': torch.tensor(input_ids, dtype=torch.long)
            })

    print(f'\n[{filepath}] スキップ: {skipped} 件 → 使用: {len(dataset)} 件\n')
    return dataset


train_path = 'mao/chapter08/SST-2/train.tsv'
dev_path = 'mao/chapter08/SST-2/dev.tsv'

train_data = load_sst_dataset(train_path, word2id)
dev_data = load_sst_dataset(dev_path, word2id)
