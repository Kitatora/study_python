# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

l1 = input()
l2 = input()
a, b = l1.split()
c, d = l2.split()
print(int(a)*int(d)-int(b)*int(c))

#Option-1
li = []
while True:
    try: #例外処理。exceptとセット
        li.append(list(map(int, input().split()))) #第一引数を第二引数に適用。
    except: #例外処理。tryの中でエラーになる場合にexceptを実行。
        break
print(li[0][0] * li[1][1] - li[0][1] * li[1][0])