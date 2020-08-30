# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

x, p = map(int, input().split())
t = 0

while x >= 1:
    t = t + x
    x = int(x*(100-p)/100)

print(t)