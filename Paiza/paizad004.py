# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

import sys
input_line = input()
for input_line in sys.stdin.readlines():
    print(",".join(input_line.rstrip()))

#実行結果：期待する結果にならず
#P,a,i,z,a
#G,i,n,o