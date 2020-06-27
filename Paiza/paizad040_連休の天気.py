# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

t_1 = int(input())
t_2 = int(input())
t_3 = int(input())
t_4 = int(input())
t_5 = int(input())
t_6 = int(input())
t_7 = int(input())
l=[t_1, t_2, t_3, t_4, t_5, t_6, t_7]
n = sum(x <= 30 for x in l)
print(n)