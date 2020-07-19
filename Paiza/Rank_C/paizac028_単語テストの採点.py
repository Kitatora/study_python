# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
l = []
score = 0
for i in range(n):
    l.append(list(map(str, input().split())))
    if l[i][0] == l[i][1]:
        score += 2
    elif len(l[i][0]) != len(l[i][1]):
        score += 0
    elif len(l[i][0]) == len(l[i][1]):
        li1 = l[i][0]
        li2 = l[i][1]
        ng = 0
        for j in range(len(l[i][0])):
            if li1[j] != li2[j]:
                ng += 1
        if ng == 0:
            score += 0
        elif ng == 1:
            if li1 != li2:
                score += 1
        elif ng >= 2:
            score +=0
print(score)
