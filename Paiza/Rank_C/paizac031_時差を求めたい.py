# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import datetime as dt

n = int(input())
li = []
for i in range(n):
    li.append(list(map(str, input().split())))

a, b = input().split() #singapore 19:38
b_time = dt.datetime.strptime(b, "%H:%M")
# print(li)
# print(i)
for i in li:
    # print(i)
    if i[0] == a:
        country = int(i[1])
# print(country)

li2 = []
for i in li:
    li2.append(int(i[1])-country)
# print(li2)

for i in range(len(li2)):
    n_time = b_time + dt.timedelta(hours = li2[i])
    str_MH = dt.datetime.strftime(n_time, "%H:%M")
    print(str_MH)

