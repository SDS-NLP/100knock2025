"""
knock75:パディング
複数の事例が与えられたとき、これらをまとめて一つのテンソル・オブジェクトで
表現する関数collateを実装せよ。
与えられた複数の事例のトークン列の長さが異なるときは、
トークン列の長さが最も長いものに揃え、0番のトークンIDでパディングをせよ。
さらに、トークン列の長さが長いものから順に、事例を並び替えよ。
"""
import torch
from torch.nn.utils.rnn import pad_sequence

def collate(batch):
    # 入力長で降順にソート
    batch.sort(key=lambda x: len(x['input_ids']), reverse=True)

    # 各項目を抽出
    input_ids_list = [item['input_ids'] for item in batch]
    labels = torch.stack([item['label'] for item in batch])  # (batch_size, 1)

    # パディング（0番トークンIDで埋める）
    padded_input_ids = pad_sequence(input_ids_list, batch_first=True, padding_value=0)

    return {
        'input_ids': padded_input_ids,
        'label': labels
    }



