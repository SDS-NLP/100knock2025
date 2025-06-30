# knock75.py
import torch
from torch.nn.utils.rnn import pad_sequence

def collate_fn(batch):
    """
    batch: list of dicts, each with keys 'input_ids' and 'label'
    return: dict with padded input_ids and stacked labels
    """
    # Sort by sequence length (descending)
    batch.sort(key=lambda x: len(x['input_ids']), reverse=True)

    input_ids = [item['input_ids'] for item in batch]
    labels = [item['label'] for item in batch]

    # Pad sequences
    input_ids_padded = pad_sequence(input_ids, batch_first=True, padding_value=0)
    labels = torch.stack(labels)

    return {'input_ids': input_ids_padded, 'label': labels}

# -----------------------------
# 動作テスト（任意）
# -----------------------------
if __name__ == "__main__":
    # 例データ（train_data[:4] などを模倣）
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

    result = collate_fn(batch)
    print("📦 input_ids:\n", result["input_ids"])
    print("✅ labels:\n", result["label"])