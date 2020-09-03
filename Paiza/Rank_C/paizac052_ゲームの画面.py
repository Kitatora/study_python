# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

h, w = map(int, input().split())
dy, dx = map(int, input().split())

d = (abs(h*dx))+(abs(w*dy))-(abs(dx*dy))
print(d)

///
入力値
100 80
95 -6

出力結果
7630
///