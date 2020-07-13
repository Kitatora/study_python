# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

#不正解。要再検討

m = int(input())
n = int(input())
li = []
for i in range(n):
    li.append(list(map(int, input().split())))


p = 0
t = 0
for i in range(n):
    if li[i][0] == 1:
        p += li[i][2]
        if p % m == 0:
            t = t + p//m
        elif p % m != 0:
            t = t + p//m + 1
    if li[i][0] == 2:
        p += li[i][2]
        if p % m == 0:
            t = t + p//m
        elif p % m != 0:
            t = t + p//m + 1
    if li[i][0] == 3:
        p += li[i][2]
        if p % m == 0:
            t = t + p//m
        elif p % m != 0:
            t = t + p//m + 1
    # if li[i][0] == 4:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 5:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 6:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 7:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 8:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 9:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 10:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 11:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 12:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 13:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 14:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 15:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 16:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 17:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 18:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 19:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 20:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 21:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 22:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1
    # if li[i][0] == 23:
    #     p += li[i][2]
    #     if p % m == 0:
    #         t = t + p//m
    #     elif p % m != 0:
    #         t = t + p//m + 1

print(t)
