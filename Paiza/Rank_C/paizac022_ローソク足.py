# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
l = []
for i in range(n):
    l.append(list(map(int, input().split())))

lmax = []
for i in range(n):
    lmax.append(l[i][2])

lmin = []
for i in range(n):
    lmin.append(l[i][3])

op = l[0][0]
cp = l[n-1][1]
ma = max(lmax)
mi = min(lmin)
print(op, cp, ma, mi)