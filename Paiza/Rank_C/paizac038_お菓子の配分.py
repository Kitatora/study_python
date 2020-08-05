# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

m, n = map(int, input().split())

li0 = [] #与えられたデータのリスト
li1 = [] #商のリスト
li2 = [] #余りのリスト

#与えられたデータのリスト
for i in range(m):
    li0.append(int(input()))

#商のリストを作成
for i in range(m):
    li1.append(n // li0[i])

#余りのリストを作成
for i in range(m):
    li2.append(n % li0[i])
print(li2)
#最初値のインデックスを返す
a = [i for i, v in enumerate(li2) if v == min(li2)]
#[0,1]
# インデックス番号を求めた所で終了。
# インデックス番号を求めた所で、どうやって値を取り出す？
# あまりの重複が複数個になった場合、どうやって全てを比較する？