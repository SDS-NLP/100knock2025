import torch
from torch.utils.data import DataLoader, Dataset
from knock71 import train_data
from knock72 import SSTDataset # train_dataはlist、SSTDatasetが必要

def collate_fn(batch):
    # input_idsの長さで降順ソート
    batch = sorted(batch, key=lambda x: len(x["input_ids"]), reverse=True)

    # 各系列のinput_idsとlabelを取り出す
    input_ids = [item["input_ids"] for item in batch]
    labels = [item["label"] for item in batch]

    # 最大長を取得してパディング
    max_len = len(input_ids[0])
    padded_ids = []
    for ids in input_ids:
        padded = torch.cat([ids, torch.zeros(max_len - len(ids), dtype=torch.long)])
        padded_ids.append(padded)

    # バッチテンソルに変換
    input_tensor = torch.stack(padded_ids)  # (batch_size, max_len)
    label_tensor = torch.stack(labels)      # (batch_size, 1)

    return {"input_ids": input_tensor, "label": label_tensor}

# Datasetをラップ（train_dataがリスト形式なのでSSTDatasetに包む）
train_dataset = SSTDataset(train_data)

# DataLoaderの作成（バッチサイズ32、シャッフルあり、collate_fn指定）
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True, collate_fn=collate_fn)
# 最初の1バッチだけ表示してみる
for batch in train_loader:
    print("input_ids:")
    print(batch["input_ids"])
    print("label:")
    print(batch["label"])
    break  # 最初の1バッチだけ