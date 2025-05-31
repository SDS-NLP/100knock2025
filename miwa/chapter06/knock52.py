#52.類似度の高い単語10件
from knock50 import model

if __name__ == "__main__":
    result = model.most_similar("United_States", topn=10) #ここで単語を指定
    print(result)