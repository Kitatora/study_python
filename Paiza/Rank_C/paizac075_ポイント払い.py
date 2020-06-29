# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

N, M = input().split()
n = int(N)
m = int(M)
poi = 0
for i in range(m):
    pay = int(input())
    n -= pay
    poi += int(pay * 0.1)
    if pay < poi:
        n += pay
        poi -= (pay + int(pay * 0.1))
    print(n, poi)

#点数70点