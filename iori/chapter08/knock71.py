from knock70 import token_to_id,id_to_token, embedding_matrix
import numpy as np
import torch

def load_data(file_path, token_to_id):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            label, text = line.strip().split('\t')
            tokens = text.split()
            input_ids = [token_to_id[token] for token in tokens if token in token_to_id]
            if input_ids:  # Skip if input_ids is empty
                data.append({
                    'text': text,
                    'label': torch.tensor([1.]) if label == '1' else torch.tensor([0.]),
                    'input_ids': torch.tensor(input_ids)
                })
    return data

train_data = load_data('SST-2/train.tsv', token_to_id)
dev_data = load_data('SST-2/dev.tsv', token_to_id)