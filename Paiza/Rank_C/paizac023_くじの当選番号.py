# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a, b, c, d, e, f = input().split()
a1 = int(a)
b1 = int(b)
c1 = int(c)
d1 = int(d)
e1 = int(e)
f1 = int(f)
li = [a1, b1, c1, d1, e1, f1]

n = int(input())

li2 = []
for i in range(n):
    li2.append(list(map(int, input().split())))
    li_li2_and = set(li) & set(li2[i])
    print(len(li_li2_and))