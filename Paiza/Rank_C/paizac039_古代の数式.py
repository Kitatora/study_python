# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a = input().split("+")
li = []
for i in range(len(a)):
    li.append(a[i].count("/")*1 + a[i].count("<")*10)
print(sum(li))

"""
<：10
/：1

入力例1
<///////+<<</+////

出力結果
52
"""