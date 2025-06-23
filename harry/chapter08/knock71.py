#71. データセットの読み込み
# General Language Understanding Evaluation (GLUE) ベンチマークで配布されているStanford Sentiment Treebank (SST) をダウンロードし、
# 訓練セット（train.tsv）と開発セット（dev.tsv）のテキストと極性ラベルと読み込み、全てのテキストをトークンID列に変換せよ。
# このとき、単語埋め込みの語彙でカバーされていない単語は無視し、トークン列に含めないことにせよ。
# また、テキストの全トークンが単語埋め込みの語彙に含まれておらず、
# 空のトークン列となってしまう事例は、訓練セットおよび開発セットから削除せよ（このため、第7章の実験で得られた正解率と比較できなくなることに注意せよ）。
# 事例の表現方法は任意でよいが、例えば”contains no wit , only labored gags”がネガティブに分類される事例は、次のような辞書オブジェクトで表現すればよい。
# {'text': 'contains no wit , only labored gags',
#  'label': tensor([0.]),
#  'input_ids': tensor([ 3475,    87, 15888,    90, 27695, 42637])}
# この例では、textはテキスト、labelは分類ラベル
# （ポジティブならtensor([1.])、ネガティブならtensor([0.])）、input_idsはテキストのトークン列をID列で表現している。

# knock71.py
import torch
from pathlib import Path

# ファイルパスの設定
DATA_DIR = Path(__file__).resolve().parent / 'SST-2'
TRAIN_FILE = DATA_DIR / 'train.tsv'
DEV_FILE = DATA_DIR / 'dev.tsv'
WORD2ID_FILE = Path('word2id.pt')

# 単語 -> ID の辞書を読み込む（knock70.pyで保存したもの）
word2id = torch.load(WORD2ID_FILE)

def tokenize(text):
    """簡単な空白トークナイズ"""
    return text.strip().lower().split()

def convert_to_ids(tokens, word2id):
    """語彙にあるトークンだけをIDに変換"""
    return [word2id[token] for token in tokens if token in word2id]

def load_dataset(file_path, word2id):
    file_path = Path(file_path)
    dataset = []
    with open(file_path, encoding='utf-8') as f:
        next(f)
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) < 2:
                continue
            text = parts[0]
            label = torch.tensor([float(parts[1])])

            tokens = tokenize(text)
            input_ids = convert_to_ids(tokens, word2id)

            if len(input_ids) == 0:
                continue

            dataset.append({
                'text': text,
                'label': label,
                'input_ids': torch.tensor(input_ids)
            })

    
    return dataset

# データの読み込み
train_data = load_dataset(TRAIN_FILE, word2id)
dev_data = load_dataset(DEV_FILE, word2id)

# 件数表示
print(f"✅ train.tsv: {len(train_data)} 件のデータを読み込みました")
print(f"✅ dev.tsv: {len(dev_data)} 件のデータを読み込みました")

# 任意：確認用に先頭の1件表示
print("\n📝 例：", train_data[0])


