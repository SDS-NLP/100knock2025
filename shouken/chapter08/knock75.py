import torch
from torch.nn.utils.rnn import pad_sequence

def collate(batch):
    """
    複数の事例（辞書）を受け取り、長さ順にソートし、
    パディングしてバッチ化されたテンソルを返す。
    """
    # ① input_idsの長さで降順に並び替え
    batch.sort(key=lambda x: len(x['input_ids']), reverse=True)

    # ② input_idsとlabelを取り出す
    input_ids_list = [item['input_ids'] for item in batch]
    labels = [item['label'] for item in batch]

    # ③ input_idsをパディングしてテンソル化
    padded_input_ids = pad_sequence(input_ids_list, batch_first=True, padding_value=0)

    # ④ labelをテンソル化（すでにtensorなのでstackするだけ）
    label_tensor = torch.stack(labels)

    return {
        'input_ids': padded_input_ids,
        'label': label_tensor
    }
