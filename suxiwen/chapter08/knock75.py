import torch
from torch.utils.data.dataloader import default_collate
#default_collate：PyTorch のデフォルトのバッチ処理関数
def collate(batch):
    """
    複数の事例をバッチ処理する関数
    
    処理内容:
    1. 事例をinput_idsの長さで降順にソート
    2. 可変長のinput_idsを0でパディングしてテンソルに変換
    3. ラベルをバッチ用のテンソルに変換
    
    Args:
        batch (list): 事例のリスト。各事例は辞書で、'input_ids'と'label'を含む。
        
    Returns:
        dict: パディングされたinput_idsとラベルのテンソルを含む辞書
    """
    # 1. input_idsの長さで降順にソート（最も長いシーケンスが先頭にくる）
    #key=lambda x: len(x['input_ids'])：各事例のinput_idsの長さを基準にソート
    #reverse=True：降順にソート
    batch.sort(key=lambda x: len(x['input_ids']), reverse=True)
    
    # 2. input_idsをリストに抽出ソート後の各事例のinput_idsをリストに集める
    input_ids_list = [example['input_ids'] for example in batch]
    
    # 3. 可変長のシーケンスをパディングして固定長のテンソルに変換
    # padding_value=0: パディングに0番のトークンIDを使っています
    # batch_first=True: 出力の形を[batch_size, sequence_length]にする
    padded_input_ids = torch.nn.utils.rnn.pad_sequence(
        input_ids_list,
        batch_first=True,
        padding_value=0
    )
    
    # 4. ラベルをデフォルトのcollate関数でバッチ用のテンソルに変換
    #[example['label'] for example in batch]：全事例のラベルを抽出
    #default_collate：デフォルトのバッチ処理を適用
    labels = default_collate([example['label'] for example in batch])
    
    return {
        'input_ids': padded_input_ids,
        'label': labels
    }

# スクリプトとして実行された時のみ処理を実行
if __name__ == "__main__":
    # テスト用のダミーデータ
    dummy_batch = [
        {
            'text': 'hide new secretions from the parental units',
            'label': torch.tensor([0.]),
            'input_ids': torch.tensor([5785, 66, 113845, 18, 12, 15095, 1594])
        },
        {
            'text': 'contains no wit, only labored gags',
            'label': torch.tensor([0.]),
            'input_ids': torch.tensor([3475, 87, 15888, 90, 27695, 42637])
        },
        {
            'text': 'that loves its characters and communicates something rather beautiful about human nature',
            'label': torch.tensor([1.]),
            'input_ids': torch.tensor([4, 5053, 45, 3305, 31647, 348, 904, 2815, 47, 1276, 1964])
        },
        {
            'text': 'remains utterly satisfied to remain the same throughout',
            'label': torch.tensor([0.]),
            'input_ids': torch.tensor([987, 14528, 4941, 873, 12, 208, 898])
        }
    ]
    
    # collate関数を実行
    result = collate(dummy_batch)
    
    # 結果を表示
    print("=== パディング後のinput_ids ===")
    print(result['input_ids'])
    print("\n=== ラベル ===")
    print(result['label'])