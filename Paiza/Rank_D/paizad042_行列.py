# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

l1 = input()
l2 = input()
a, b = l1.split()
c, d = l2.split()
print(int(a)*int(d)-int(b)*int(c))

#Option-1
li = []
while True: #whileは「while 条件文：」構文にて条件文がブール値Trueの時に下記の処理文を返す。
            #では、whileの条件文に最初からTrueを与えると・・・。
            #条件文が常に"真"となるため、処理文が延々繰り返されることになる！
    try: #例外処理。exceptとセット
        li.append(list(map(int, input().split()))) #第一引数を第二引数に適用。
        #map関数： map(関数, 配列オブジェクト)。　配列オブジェクトの各値に対し、指定した"関数"を実行する。
        #配列オブジェクト：文字列、リスト、辞書等
    except: #例外処理。tryの処理文がエラーになる場合にexceptの処理文を実行。
        break
print(li[0][0] * li[1][1] - li[0][1] * li[1][0])

"""
Option-1の流れ
☆配列オブジェクトをリスト化することで、リスト内包型リストを作成。li[インデックス番号1][インデックス番号2]で値を取り出せるようにする。

①map関数によって中の配列オブジェクトに関数intを適用した後、イテラル化。
②map関数の中身をlist関数にてリスト化。
③予め作成していた空リストliに代入
③inputされるデータの個数が不明なため、While True:で以下Try構文の処理を無限ループさせ、exceptとなった場合（tryがエラー、つまりinputから入力されるデータが無くなった場合）、ループ
"""