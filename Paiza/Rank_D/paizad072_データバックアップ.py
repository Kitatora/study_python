# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

x, y, p = input().split()
X = int(x)
Y = int(y)
P = int(p)
if X % Y == 0:
    print(X // Y * P)
elif X % Y != 0:
    print((X // Y + 1) * P)