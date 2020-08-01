# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
li = []
p = 0
for i in range(n):
    li.append(list(map(str, input().split())))
    if int(li[i][1]) + int(li[i][2]) + int(li[i][3]) + int(li[i][4]) + int(li[i][5]) >= 350:
        if li[i][0] == "s":
            if int(li[i][2]) + int(li[i][3]) >= 160:
                p += 1
        elif li[i][0] == "l":
            if int(li[i][4]) + int(li[i][5]) >= 160:
                p += 1
print(p)            
