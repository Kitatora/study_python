#encoding:utf-8
import random

a1 = random.randint(0, 9)
a2 = random.randint(0, 9)
a3 = random.randint(0, 9)
a4 = random.randint(0, 9)
list_a = [a1, a2, a3, a4]
print(list_a)

b = input("数を入れてね>")
print(b[0])
print(b[1])
print(b[2])
print(b[3])
if a == b:
    print("正解です")
else:
    print("間違いです")