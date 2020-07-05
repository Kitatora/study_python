# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

N, M = input().split()
n = int(N)
m = int(M)
if n%2==0 and m%2==0:
    print("NO")
elif n%2==1 and m%2==1:
    print("NO")
else:
    print("YES")