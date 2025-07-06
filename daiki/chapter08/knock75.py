import torch
import torch.nn.utils.rnn as rnn_utils

def collate_batch(batch):
    # 1. まず長さを取得してソート
    sorted_batch = sorted(batch, key=lambda x: len(x["input_ids"]), reverse=True)
    
    # 2. input_ids と label をリストにまとめる
    input_ids_list = [item["input_ids"] for item in sorted_batch]
    labels_list = [item["label"] for item in sorted_batch]
    
    # 3. pad_sequence でパディング
    # デフォルトは右側パディング
    input_ids_padded = rnn_utils.pad_sequence(
        input_ids_list,
        batch_first=True,
        padding_value=0
    )
    
    # labels は結合するだけで良い
    labels_tensor = torch.stack(labels_list, dim=0)
    
    return {
        "input_ids": input_ids_padded,
        "label": labels_tensor
    }

batch = [
    {'text': 'hide new secretions from the parental units',
     'label': torch.tensor([0.]),
     'input_ids': torch.tensor([5785, 66, 113845, 18, 12, 15095, 1594])},
    {'text': 'contains no wit , only labored gags',
     'label': torch.tensor([0.]),
     'input_ids': torch.tensor([3475, 87, 15888, 90, 27695, 42637])},
    {'text': 'that loves its characters and communicates something rather beautiful about human nature',
     'label': torch.tensor([1.]),
     'input_ids': torch.tensor([4, 5053, 45, 3305, 31647, 348, 904, 2815, 47, 1276, 1964])},
    {'text': 'remains utterly satisfied to remain the same throughout',
     'label': torch.tensor([0.]),
     'input_ids': torch.tensor([987, 14528, 4941, 873, 12, 208, 898])}
]

batch_out = collate_batch(batch)

print(batch_out)
