# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

s, a, b = map(int, input().split())
p = s

while (p >= a) or (p <= b):
    p += 10
    if p + 1000 > b:
        print("A", p)
        break
    p += 1000
    if p + 10 > a:
        print("B", p)
        break

    ///
    入力値
    1 1500 2050

    出力
    B 2021
    ///