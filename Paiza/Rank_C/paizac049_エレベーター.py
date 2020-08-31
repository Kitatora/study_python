# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

floors = li[0]-1

for i in range(n-1):
    floors = floors + abs((li[i+1]-li[i]))

print(floors)


///
入力2
8
17
28
11
62
64
4
7
17
答え
170
///