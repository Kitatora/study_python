# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

l = list(map(int, input().split()))
a = sorted(l)[-1]
b = sorted(l)[-2]
c = sorted(l)[-3]
d = sorted(l)[-4]
num1 = str(a)+str(c)
num2 = str(b)+str(d)
print(int(num1)+int(num2))

#ループを使ってa〜dの全ての組み合わせを試し、その中から最大値を得る方法はどうする？