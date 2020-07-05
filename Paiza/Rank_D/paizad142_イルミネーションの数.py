#encoding:utf-8

l = list(map(int, input().split()))
if l[0]%l[1] == 0:
    print((l[0]//l[1])*l[2])
elif l[0]%l[1] != 0:
    print((l[0]//l[1]+1)*l[2])