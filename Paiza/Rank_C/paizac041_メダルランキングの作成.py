# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

m = int(input())
li1 = []

for i in range(m):
    li1.append(list(map(int, input().split())))
li1.sort(reverse = True)
for i in li1:
    a, b, c = i
    print(a, b, c)

"""
二次元配列のsortがキー。
二次元配列にsortするだけで、index番号1の昇順、番号2の昇順、番号3の昇順（優先順位：番号1>2>3）となる。
reverse = Trueとすると、降順のリストとなる。

入力例1
6
3 5 9
15 20 35
30 45 72
15 20 31
27 33 59
27 35 77

出力結果
30 45 72
27 35 77
27 33 59
15 20 35
15 20 31
3 5 9

"""