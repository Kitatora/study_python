#encoding:utf-8

from random import randrange

x = randrange(0, 10, 1)
flag = True
while flag: #基本ルールとして、whileはTrueの場合に繰り返す。flag = Trueとすることで、強制的に繰り返しを発生させる
    print(x)
    if x > 8:
        break #ここまでだと、一度print(x)に入った数字を（コード上9を除く）無限ループさせる。
    else:
        x = randrange(0, 10, 1) #9が出ない限り、else文を実行させる。

#9がランダム選択された時点でループが止まるコードになる
#まとめ：whileはFalseかbreakが出るまでwhile内のコードを実行させる