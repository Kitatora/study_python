# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

a, b = map(int, input().split())
c, d = map(int, input().split())

li = list(map(int, input().split()))
li2 = list(map(int, input().split()))
li_win = []
if li[a-1] > li[b-1]:
    li_win.append(b)
elif li[a-1] < li[b-1]:
    li_win.append(a)
if li[c-1] > li[d-1]:
    li_win.append(d)
elif li[c-1] < li[d-1]:
    li_win.append(c)
# print(li_win) #[3,2]
li_win2 = sorted(li_win)
# print(li_win2) #[2,3]
if li2[0] < li2[1]:
    print(li_win2[0])
    print(li_win2[1])
if li2[0] > li2[1]:
    print(li_win2[1])
    print(li_win2[0])
