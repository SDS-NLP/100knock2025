import torch

def collate(batch):
    # トークン長でソート
    batch.sort(key=lambda x: len(x['input_ids']), reverse=True)
    
    # 最大長を取得
    max_len = len(batch[0]['input_ids'])

    # パディングとテンソル化
    padded_input_ids = []
    labels = []

    for item in batch:
        ids = item['input_ids']
        pad_len = max_len - len(ids)
        padded = torch.cat([ids, torch.zeros(pad_len, dtype=torch.long)])
        padded_input_ids.append(padded)
        labels.append(item['label'])

    return {
        'input_ids': torch.stack(padded_input_ids),
        'label': torch.stack(labels)
    }
