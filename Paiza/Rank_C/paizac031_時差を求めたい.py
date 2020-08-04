# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！import datetime

# n = int(input())
# li = []
# for i in range(n):
#     li.append(list(map(str, input().split())))
# a, b = input().split()
# b_time = datetime.datetime.strptime(b, "%H:%M")
# # print(li)
# print(b_time)
# li2 = []
# for i in range(1, n+1):
#     li2.append(li[i-1][1])
# print(li2)
# li3 = list(map(int, li2))
# for i in range(len(li3)):
#     n_time = b_time + datetime.timedelta(li3[i])
#     print(n_time)

# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import datetime as dt

n = int(input())
li = []
for i in range(n):
    li.append(list(map(str, input().split())))

print(li)
a, b = input().split()
print(a)
print(b)
# b_time = dt.datetime(b, "%H:%M")
b_time = dt.datetime.strptime(b, "%H:%M").time
# t1=datetime.strptime('09:00:00','%H:%M:%S').time()
print(b_time)
# # print(li)
# # print(b_time)
# li2 = []
# for i in range(1, n+1):
#     li2.append(li[i-1][1])
# print(li2)
# li3 = list(map(int, li2)) 
# for i in range(len(li3)):
#     n_time = b_time + datetime.timedelta(hours = li3[i])
#     print(n_time)
    #時間と分を出力する方法を調べる
    #時差の算出方法を再確認

