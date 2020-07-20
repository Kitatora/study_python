# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a,b = input().split()
n = int(a)
d = int(b)
li = []

for i in range(n):
    li.append(list(map(int, input().split())))

#スライスでd個の要素が入ったリストを作成し、そこから平均値を算出
li2 = []
for j in range(d):
    li2.append(li[j:j+d-1])
print(li2)

