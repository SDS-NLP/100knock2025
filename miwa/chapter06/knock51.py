#51.単語の類似度
from knock50 import model

if __name__ == "__main__":
    result = model.similarity("United_States", "U.S.") #ここで単語を指定
    print(result)