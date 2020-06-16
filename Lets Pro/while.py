#encoding:utf-8
#Example-1
num = 0
while num < 2:
    print("num = " + str(num))
    num += 1
print("End")


# 1) 変数 num に 0 を代入
# 2) while 文の条件式を評価。変数 num は 2 より小さいので条件式は真
# 3) 変数 num の値を出力
# 4) 変数 num に 1 を加算 (num は 1)
# 5) ブロックの最後まで達したので再度 while 文の条件式を評価
# 6) 変数 num は 2 より小さいので条件式は真
# 7) 変数 num の値を出力
# 8) 変数 num に 1 を加算 (num は 2)
# 9) ブロックの最後まで達したので再度 while 文の条件式を評価
# 10) 変数 num は 2 より小さくないので条件式は偽
# 11) while 文を終了し次の処理へ
# 12) "End" を出力


#Example-2
num = 2
while num <= 10:
    print("num = " + str(num))
    num += 1

print("End")

#Example-3
num = 1
total = 0
print("Start")

while num < 6:
    print("num = " + str(num))
    total += num
    num += 1
else:
    print("Total = " + str(total))

print("End")