def cipher(text):
    """
    ・英小文字ならば (219 - 文字コード) のASCIIコードに対応する文字に置換
    ・その他の文字はそのまま出力
    """
    answer=""
    for w in text:
        if w.islower():
            answer+=chr(219-ord(w))
        else:
            answer+=w
    return answer

#結果確認
print("暗号化：",cipher("hello")) #暗号化
print("復号化：",cipher("svool")) #復号化
