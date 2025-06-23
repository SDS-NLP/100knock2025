#65. テキストのポジネガの予測
from knock61 import dev_data
from knock62 import clf, vectorizer, label_encoder

def extract_features(sentence):
    tokens = sentence.strip().split()
    feature = {}
    for token in tokens:
        feature[token] = feature.get(token, 0) + 1 #.get(key,0)でkeyに対応する値を返す、keyなければ0を返す
    return feature

def positive_or_negative(example):
    feature_dict=extract_features(example)
    # 特徴ベクトルに変換（DictVectorizerで整形）
    X_example = vectorizer.transform([feature_dict])

    # ラベル予測
    pred_label_num = clf.predict(X_example)[0]                # 数値ラベル（例: 0 or 1）
    pred_label = label_encoder.inverse_transform([pred_label_num])[0]  # 元のラベルに変換（例: '0' or '1'）

    # 結果
    return pred_label

example="the worst movie I ‘ve ever seen"
pred_label=positive_or_negative(example)
print("テキスト:", example)
print("予測ラベル:", pred_label)