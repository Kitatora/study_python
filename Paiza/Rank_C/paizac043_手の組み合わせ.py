# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
import collections

n = int(input())
li = []
for i in range(n):
    li.append(input())
#["r", "p", "r", "s"]
a = collections.Counter(li)
#print(a)
#   Counter({"r":2, "p":1, "s":1}
#print(len(a))
#   3
if len(a) == 3:
    print("draw")
elif len(a) == 1:
    print("draw")
elif len(a) == 2:
    if "rock" not in a:
        print("scissors")
    elif "scissors" not in a:
        print("paper")
    elif "paper" not in a:
        print("scissors")

"""
入力1
4
rock
paper
rock
scissors

出力1
draw
"""
