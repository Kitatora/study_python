#coding:utf-8
#正規表現による一発チェック　re.match(r^ ~~~ $, 変数)　^:文頭、　$:文末、\d: 数字かどうかをチェック
import re

num = False 
while num == False:　　
    b = input("数を入れてください>")
    if not re.match(r"^\d\d\d\d$", b):
        print("4桁の数字を入力してください")
    else:
        num = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])
