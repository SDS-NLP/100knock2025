"""
knock32:AのB
testにおいて、2との名詞が「の」で連結されている名詞句を
全て抽出せよ
"""
text = """
メロスは激怒した。
必ず、かの邪智暴虐の王を除かなければならぬと決意した。
メロスには政治がわからぬ。
メロスは、村の牧人である。
笛を吹き、羊と遊んで暮して来た。
けれども邪悪に対しては、人一倍に敏感であった。
"""
import MeCab

tagger=MeCab.Tagger("-r /opt/homebrew/etc/mecabrc -Owakati")
node=tagger.parseToNode(text)

triplet=[]       #直近3単語を保持するリスト
noun_phrases=[]  #抽出された名詞句を入れるリスト

while node:
    surface=node.surface            #単語そのもの
    feature=node.feature.split(",") #品詞などを含むCSV

    #必要な情報だけ取り出してtirpletに追加　
    triplet.append((surface,feature[0])) #表層系と品詞を追加

#3語ずつ調べる方法　
#tripletに3語貯まったらチェックを開始
    if len(triplet) ==3:
        if (triplet[0][1]=="名詞" and  #品詞が[名詞]
            triplet[1][0]=="の" and    #単語が[の]
            triplet[2][1]=="名詞"):    #品詞が[名詞]
            phrase=triplet[0][0]+triplet[1][0]+triplet[2][0]
            noun_phrases.append(phrase)
        triplet.pop(0)   #先頭を消去（スライド)

    #次の形態素へ進む
    node=node.next

print(noun_phrases)