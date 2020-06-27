# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

Name, Gender = input().rsplit()
if Gender == "F":
    print("Hi, Ms. " + Name)
elif Gender == "M":
    print("Hi, Mr. " + Name)