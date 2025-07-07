#75. パディング
import torch
from torch.nn.utils.rnn import pad_sequence
from knock71 import train_dataset

def collate(batch):
    #トークンの長さで長い順にソート
    batch.sort(key=lambda x: len(x["input_ids"]), reverse = True)

    #各項目をまとめて取得
    input_ids = [item["input_ids"] for item in batch]
    labels = [item["label"] for item in batch]

    #パディング
    padded_input_ids = pad_sequence(input_ids, batch_first=True, padding_value=0)
    #ラベルも一つのテンソルにする
    label_tensor = torch.stack(labels)

    return {
        "input_ids" : padded_input_ids, #(バッチ数, 最大長)
        "label" : label_tensor #(バッチ数, 1)
    }

#試してみる
if __name__ == "__main__":
    example = train_dataset[:4]
    print(collate(example))