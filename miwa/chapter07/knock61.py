#61. 特徴ベクトル
def extract_features(file_path):
    data = []
    with open(file_path, "r", encoding='utf-8') as f:
        next(f) #一行目(ヘッダー行)をスキップ
        for line in f:
            line = line.strip()
            try:
                text, label = line.split('\t')
            except ValueError:
                print(f"Skipping line: {line}")
                continue
            tokens = text.split()
            feature = {}
            for token in tokens:
                feature[token] = feature.get(token, 0) + 1 #.get(key,0)でkeyに対応する値を返す、keyなければ0を返す
            data.append({'text': text, 'label': label, 'feature': feature})
    return data

# BoWベースで変換
train_data = extract_features("SST-2/train.tsv")
dev_data = extract_features("SST-2/dev.tsv")

if __name__ == "__main__":
    # 学習データの最初の事例を表示して目視確認
    print("学習データの最初の事例:")
    print(train_data[0])