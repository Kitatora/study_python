# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
l = []
for i in range(n):
    cal = n - i
    l.append(cal)
cal = sum(l)
print(cal)

#Option-1
n = int(input())
total = 0
for i in range(n):
    total += n - i
print(total)