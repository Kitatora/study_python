# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input=(
5 25
80 11
20 1
)

N, M = input().split()
n = int(N)
m = int(M)
li = []
for i in range(n):
    li.append(list(map(int, input().split())))
#この時点でprint(li)を行うと、多次元配列[[5,25], [80, 11], [20, 1]]を返す
    judge = li[i][0]- li[i][1]*5
    if judge < 0:
        judge = 0
    elif judge >= 0:
        judge = judge
    if judge >= m:
        print(i + 1)
    elif judge < m:
        None
    #16行目から26行目の流れをn回繰り返す