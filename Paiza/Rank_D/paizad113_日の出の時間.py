# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

h, m = input().split(":")
if int(h) < 8:
    getup = 24 - (8 - int(h))
if int(h) >= 8:
    getup = int(h) - 8
t = ":".join([str(getup),m])
print(t)