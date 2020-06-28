# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
rp = input()
rs = rp.count("G")
ps = rp.count("P")
if rs > ps:
    print("P")
elif rs < ps:
    print("G")
elif rs == ps:
    print("Draw")