# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

n = int(input())
v_1 = 0
v_2 = 0
for i in range(n):
    s = input()
    if "SET" in s:
        c_SET, v_SET, a_SET = s.split()
        if int(v_SET) == 1:
            v_1 = int(a_SET)
        elif int(v_SET) == 2:
            v_2 = int(a_SET)
    elif "ADD" in s:
        c_ADD, n_ADD = s.split()
        v_2 = v_1 + int(n_ADD)
    elif "SUB" in s:
        c_SUB, n_SUB = s.split()
        v_2 = v_1 - int(n_SUB)
print(v_1, v_2)


li = []
while True:
    try:
        li.append(list(map(str, input().split())))
    except:
        break
li2 = []
for i in range(1, int(li[0][0]) + 1):
    li2.append(li[i])
x = 0
y = 0
for i in range(int(li[0][0])):
    if li2[i][0] == "SET":
        if int(li2[i][1]) == 1:
            x = li2[i][2]
        elif int(li2[i][1]) == 2:
            y = li2[i][2]
    elif li2[i][0] == "ADD":
        y = int(x) + int(li2[i][1])
    elif li2[i][0] == "SUB":
        y = int(x) - int(li2[i][1])
print(str(x) + " " + str(y))
    