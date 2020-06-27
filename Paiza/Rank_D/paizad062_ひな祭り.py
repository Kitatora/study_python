# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

h1, h2, h3 = input().split()
dools = "ABCDEFGHIJ"
s1 = dools[:int(h1)]
s2 = dools[int(h1):int(h1)+int(h2)]
s3 = dools[int(h1)+int(h2):int(h1)+int(h2)+int(h3)]
print(s1)
print(s2)
print(s3)