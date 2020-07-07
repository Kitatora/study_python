# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

"""
①n, m, kを取り出す
②ポイント専用のリストli1を作る
③for i in range(m):でプレイヤーm人の道具所有数を含む、リストli2を作る。
④li1[0]×li2[0], li1[1]×li2[1]....をn回繰り返し、li3にいれて合計値を計算する。


"""

N, M, K = input().split()
n = int(N)
m = int(M)
k = int(K)
li1 = list(input().split())
print(li1)
li2 = []
for i in range(m):
    li2.append(input().split())
print(li2)