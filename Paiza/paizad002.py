#encoding=utf-8
input = 10, 20
a,b = input().split()
if int(a) == int(b):
    print('eq')
elif int(b) < int(a):
    print(a)
else:
    print(b)