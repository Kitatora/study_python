# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

l1 = list(map(int, input().split()))
n = int(input())
l2 = []
for i in range(n):
    l2.append(list(map(int, input().split())))

for i in range(n):
    if l1[0] > l2[i][0]:
        print("High")
    elif l1[0] < l2 [i][0]:
        print("Low")
    elif l1[0] == l2[i][0]:
        if l1[1] > l2[i][1]:
            print("Low")
        if l1[1] < l2[i][1]:
            print("High")