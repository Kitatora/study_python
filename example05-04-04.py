#encoding:utf-8
import random

num = False
while num == Fales:
    b = input("数を入れてね>")
    if len(b) !=4:
        print("4桁の数字を入れてください")
    else:
        numok = True
        for i in range(4):
            if (b[i] < "0" or b[i] > "9") :
                print("正しい数字を入れてください")
                numok = False
                break
            if number : 
                numok = True
print(b[0])
print(b[1])
print(b[2])
print(b[3])