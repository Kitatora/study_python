# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

d, t = input().split()
d2 = d.split("/")
t2 = t.split(":")
if int(t2[0]) >= 24:
    d3 = int(d2[1]) + 1
    t3 = int(t2[0]) - 24
    print(d2[0] + "/" + str(d3) + " " + str(t3) + ":" + t2[1])
elif int(t2[0]) < 24:
    print(d2[0] + "/" + str(d2) + " " + str(t2) + ":" + t2[1])

# 入力値 01/27 24:30　→　01/28 0:30　（答え：01/28 0:30）
# 入力値 02/31 73:59　→　02/32 49:59 (答え：02/34 01:59)
# 入力値 12/31 00:00　→　12/['12', '31'] ['00', '00']:00 （答え：12/31 00:00）
# 入力値 12/31 25:01　→　12/32 1:01 （答え：12/32 01:01）


