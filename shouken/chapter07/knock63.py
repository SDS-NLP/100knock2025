from knock61 import dev_data
from knock62 import model  # knock62.pyで定義したPipeline

# 検証データの先頭事例
example = dev_data[0]
feature = example['feature']
true_label = int(example['label'])

# 予測
predicted_label = model.predict([feature])[0]

# 結果表示
print(f"テキスト: {example['text']}")
print(f"正解ラベル: {true_label}")
print(f"予測ラベル: {predicted_label}")

if predicted_label == true_label:
    print("一致しています（正解）")
else:
    print("一致していません（不正解）")
