#encoding:utf-8


n,s = input().split()
n = 10
s = "km"
if s == "km":
    mm = int(n)*1000000
elif s == "m":
    mm = int(n)*1000
elif s == "cm":
    mm = int(n)*10
print(mm)