import torch
from typing import List, Dict


def collate(batch: List[Dict]) -> Dict[str, torch.Tensor]:
    # バッチ内の最大トークン数を取得
    max_len = max(len(item["input_ids"]) for item in batch)

    # 入力テンソルとラベルテンソルを初期化
    batch_size = len(batch)
    input_tensor = torch.zeros((batch_size, max_len), dtype=torch.long)
    label_tensor = torch.zeros((batch_size, 1), dtype=torch.float)

    # 各事例の長さを取得
    lengths = [len(item["input_ids"]) for item in batch]

    # 長さでソートするためのインデックスを取得
    sorted_indices = sorted(range(batch_size), key=lambda i: lengths[i], reverse=True)

    # パディングとソートを実行
    for i, idx in enumerate(sorted_indices):
        item = batch[idx]
        input_tensor[i, : len(item["input_ids"])] = item["input_ids"]
        label_tensor[i] = item["label"]

    return {"input_ids": input_tensor, "label": label_tensor}
