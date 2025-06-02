#53.加法構成性によるアナロジー
from knock50 import model

if __name__ == "__main__":
    #新しいベクトルを計算
    new_vec = model["Spain"] - model["Madrid"] + model["Athens"]

    result = model.most_similar(new_vec, topn=10) #ここで単語を指定
    print(result)