# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

t, m = input().split()
T = int(t)
M = int(m)
if T >= 25 or M <= 40:
    print("Yes")
elif T >= 25 and M <= 40:
    print("No")
else:
    print("No")