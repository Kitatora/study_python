# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

"""
①n、mを取り出す
Option-1
②forとin演算子を用いて、nに一致する数字を出力
※上記やり方では、全て一致しない場合"none"一語だけを返す方法がわからないので、Option-2(③以降)に方針変更

Option-2
③部屋番号rをリスト化し、all関数で全て不一致の場合は"none"を返すようにする
"""

n = input()
m = int(input())
l = []
#Option-1
# for i in range(2, m+2):
#     r = input()
#     if str(n) not in r:
#         print(r)

#Option-2
for i in range(2, m+2):
    l.append(input())
    if n in l:
        print(l)
    elif all(x == n for x not in l):
        print("none")