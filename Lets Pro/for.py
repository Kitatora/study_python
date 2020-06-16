#encoding:utf-8
num = 1
mylist = ["A", "B", "C"]
for number in mylist:
    print(number)
print("End")

#  1) リストを定義し変数 mylist にを代入
#  2) mylist から要素を 1 つ取得して val に代入 (val は "Orange")
#  3) 変数 val の値を出力
#  4) mylist から要素を 1 つ取得して val に代入 (val は "Peach")
#  5) 変数 val の値を出力
#  6) mylist から要素を 1 つ取得して val に代入 (val は "Lemon")
#  7) 変数 val の値を出力
#  8) イテラブルオブジェクトから要素をすべて取得したので for 文を終了
#  9) "End" を出力

#sample-3
mylist = ["Orange", "Peach", "Lemon", "Apple"]
print(mylist)
for val in mylist:
    print("value:" + val)

print("¥n")

mydict = {"L":"Lemon", "O":"Orage", "G":"Grapes"}
print(mydict)
for mykey, myvalue in mydict.items():
    print("key:" + mykey + ", value:" + myvalue)