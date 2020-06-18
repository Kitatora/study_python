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

list1 = ["a", "b", "c"]
list1.extend(["d", "e"])
print(list1)
#["a", "b", "c", "d", "e"]

list2 = ["a", "b", "c"]
list2.append(["d","e"])
print(list2)
#["a", "b", "c", ["d", "e"]]