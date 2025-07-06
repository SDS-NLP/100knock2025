from knock71 import train_data, dev_data
import torch

def collate(data):
    # バッチ内の最大長を取得
    max_length = max(len(item['input_ids']) for item in data)
    
    # input_idsとlabelを収集
    input_ids_list = []
    label_list = []
    
    for item in data:
        # input_idsをパディング
        input_ids = item['input_ids'].tolist()
        padded_input_ids = input_ids + [0] * (max_length - len(input_ids))
        input_ids_list.append(padded_input_ids)
        
        # labelを収集
        label_list.append(item['label'].tolist())
    
    # テンソルに変換
    return {
        'input_ids': torch.tensor(input_ids_list),
        'label': torch.tensor(label_list)
    }

train_data_collated = collate(train_data)
dev_data_collated = collate(dev_data)

if __name__ == "__main__":
    print(train_data_collated)
    print(dev_data_collated)






