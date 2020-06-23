#encoding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

m,n = input().split() 
m = 3
n = 3
l = []
for i in range(10):
    seq = int(m) + int(n) * int(i)
    l.append(seq)
l_all = " ".join(str(x) for x in l)
print(l_all)