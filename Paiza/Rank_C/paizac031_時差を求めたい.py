# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！import datetime

n = int(input())
li = []
for i in range(n):
    li.append(list(map(str, input().split())))
a, b = input().split()
b_time = datetime.datetime.strptime(b, "%H:%M")
# print(li)
print(b_time)
li2 = []
for i in range(1, n+1):
    li2.append(li[i-1][1])
print(li2)
li3 = list(map(int, li2))
for i in range(len(li3)):
    n_time = b_time + datetime.timedelta(li3[i])
    print(n_time)