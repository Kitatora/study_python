#関数導入前
x1 = 'たろう'
y1 = 0
for i in x1:
    print(i) #"た""ろ""う"　文字列を一つずつ出力する
    y1 += 1 #1文字出力される度にy1に1を追加する
print(y1)
x2 = 'さぶろう'
y2 = 0
for i in x2:
    y2 += 1
print(y2)
x3 = 'ごろう'
y3 = 0
for i in x3:
    y3 += 1
print(y3)

#関数導入したコード
def text_len():
    length = 0
    for i in text:
        length += 1 #インデントしてるため、forが実行される度に23行目が作動する
    return length

x1 = "たろう"
x2 = "さぶろう"
x3 = "ごろう"
print(text_len(x1))
print(text_len(x2))
print(text_len(x3))
#len()でもok