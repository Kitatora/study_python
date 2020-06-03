# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input()
for word in input_line.readlines():
    print(",".join(word.rstrip()))

#実行結果：期待する結果にならず
#P,a,i,z,a
#G,i,n,o