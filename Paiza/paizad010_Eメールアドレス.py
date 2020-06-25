#encoding:utf-8

#input()
#文字列1
#文字列2

s = input()
s1 = input()
print(s + "@" + s1)


# 7行目で文字列1が、8行目で文字列2が代入されるのはなぜ？　7行目、8行目共に文字列1ではないのか？
# A. input情報が複数行の場合：input関数を実行する"度に"上から順にinputされる