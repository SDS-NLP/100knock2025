from transformers import GPT2LMHeadModel, GPT2Tokenizer
import torch

def calculate_perplexity(sentence, model, tokenizer):
    # 入力文をトークン化
    inputs = tokenizer(sentence, return_tensors="pt")
    input_ids = inputs["input_ids"]

    # 損失を計算
    with torch.no_grad():
        outputs = model(input_ids, labels=input_ids)
        loss = outputs.loss

    # パープレキシティを計算
    perplexity = torch.exp(loss)
    return perplexity.item()

def main():
    # 事前学習済みのGPT-2モデルとトークナイザーをロード
    model_name = "gpt2"
    model = GPT2LMHeadModel.from_pretrained(model_name)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    # 評価する文
    sentences = [
        "The movie was full of surprises",
        "The movies were full of surprises",
        "The movie were full of surprises",
        "The movies was full of surprises"
    ]

    # 各文のパープレキシティを計算して表示
    for sentence in sentences:
        perplexity = calculate_perplexity(sentence, model, tokenizer)
        print(f"Sentence: \"{sentence}\" | Perplexity: {perplexity}")

if __name__ == "__main__":
    main()

