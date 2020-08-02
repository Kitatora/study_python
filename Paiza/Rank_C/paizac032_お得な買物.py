# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
li = []
f = 0
b = 0
c = 0
o = 0

for i in range(n):
    li.append(list(map(int, input().split())))
    if li[i][0] == 0:
        f += li[i][1]
    elif li[i][0] == 1:
        b += li[i][1]
    elif li[i][0] == 2:
        c += li[i][1]
    elif li[i][0] == 3:
        o += li[i][1]

point = (f // 100 * 5) + (b // 100 * 3) + (c // 100 * 2) + (o // 100 * 1)
print(point)