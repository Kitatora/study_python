# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

"""
3つの条件
①4つの数字が入っている
②4つの数字が"."で区切られている
③4つの数字が0以上、255以下
"""

n = int(input())
for i in range(n):
    l = list(input().split("."))
    l.insert(1, ".")
    l.insert(3, ".")
    l.insert(5, ".")
    #②4つの数字が","でくぎられていることを確認
    if l[1] == "." and l[3] == "." and l[5]== ".":
    #③4つの数字が0以上、255以下であること、および①4つの数字が入っている事を確認
        if 0 <= int(l[0]) <= 255 and 0 <= int(l[2]) <= 255 and 0 <= int(l[4]) <= 255 and 0 <= int(l[6]) <= 255:
            print("True")
        else:
            print("False")
    else:
        print("False")
        
"""
下記引用時
  File "Main.py", line 21, in <module>
    if 0 <= int(l[0]) <= 255 and 0 <= int(l[2]) <= 255 and 0 <= int(l[4]) <= 255 and 0 <= int(l[6]) <= 255:
ValueError: invalid literal for int() with base 10: ''
→intの引数が"."になるためエラー。4つの数字が入っている事を判定するコードが先。
4
192.400.1.10.1000...
4.3.2.1
0..33.444...
1.2.3.4
"""