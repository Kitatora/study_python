# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

M = int(input())
N = int(input())
if N % M == 0:
    print(N // M)
elif N % M !=0:
    print(N // M + 1)