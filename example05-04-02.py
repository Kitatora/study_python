#encoding:utf-8
import random
num = False

while num == False:
    b = input("数を入れてね>")
    if len(b) != 4:
        print("4桁の数字を入力して下さい")
    else:
        num = True

print(b[0])
print(b[1])
print(b[2])
print(b[3])