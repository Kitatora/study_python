# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import math

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))
p = 0
for i in range(n):
    if "3" in str(l[i][0]):
        p += math.floor(l[i][1] * 0.03)
    elif "5" in str(l[i][0]):
        p += math.floor(l[i][1] * 0.05)
    else:
        p += math.floor(l[i][1] * 0.01)
print(p)
        