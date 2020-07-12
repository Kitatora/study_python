# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a, b, c, d = input().split()
xc = int(a)
yc = int(b)
r1 = int(c)
r2 = int(d)
l = []
n = int(input())
for i in range(n):
    l.append(list(map(int, input().split())))

for i in range(n):
    if r1**2  <= (l[i][0] - xc)**2 + (l[i][1] - yc)**2 <= r2**2:
        print("yes")
    else:
        print("no")