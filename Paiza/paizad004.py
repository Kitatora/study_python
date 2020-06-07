# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input()) #input情報が複数行の場合：input関数の"度に"上から順にinputされる
s = []
for i in range(n):
    s.append(input())
print(s)
print("Hello " + ",".join(s) + ".")

