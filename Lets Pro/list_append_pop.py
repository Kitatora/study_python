#encoding:utf-8

#appendメソッドを用いたリストの追加
mylist = ["Blue", "Red", "Green"]
print(mylist)

# "White" を追加
mylist.append("White")
print(mylist)

# "Black" を追加
mylist.append("Black")
print(mylist)

#スライス機能を用いたリストの追加
kantoulist = ["Tokyo", "Kanagawa", "Chiba", "Gunma"]
print(kantoulist)
addlist = ["Saitama", "Ibaraki", "Tochigi"]
print(addlist)
# kantoulist に addlist の要素を追加する
kantoulist[len(kantoulist):len(kantoulist)] = addlist #len()の値は"4"。なのでリスト番号4（16行時点ではブランク）にaddlistが追加される
print(kantoulist)