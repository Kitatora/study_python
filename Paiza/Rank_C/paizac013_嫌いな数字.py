# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
m = int(input())
a = []
for i in range(m):
    a.append(int(input()))
a.insert(0, n)
a.insert(1, m)
li = []
for i in range(2, a[1] + 2):
    li.append(a[i])
c = 0 #フラグ
for i in range(a[1]):
    if (str(li[i]).count(str(n)) == 0):
        print(li[i])
        c += 1
if c == 0: #最後にフラグの結果を見る
    print("none")