#encoding:utf-8
#x is y       x と y が同じオブジェクトの場合は True
#x not is y   x と y が別のオブジェクトの場合は True
#同じオブジェクトとは？　"=" で一致することが証明されたオブジェクト

#Pattern-1
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1 == list2 #True
type(list1)
list1 is list2 #False
type(list1)

#Pattern-2
list3 = [1, 2, 3]
list4 = list3
list3 == list4 #True
type(list3)
list3 is list4 #True
type(list3)