# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = int(input())
li1 = []
li_le = []
li_ge = []

for i in range(a):
    li1.append(list(input().split()))
    if li1[i][0] == "le":
        li_le.append(float(li1[i][1]))
    elif li1[i][0] == "ge":
        li_ge.append(float(li1[i][1]))
m = min(li_le)
M = max(li_ge)
print(M, m)