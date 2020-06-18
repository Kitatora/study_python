#encoding:utf-8
#pattern-1
mylist = []
for i in range(1, 4):
    sublist = []
    for j in range(1,3):
        sublist.append(i * 10 + j)
    mylist.append(sublist)

#上記リストを内包表現を使って書く
mylist = [[i * 10 + j for j in range(1,3)] for i in range(1, 4)]
print(mylist)
#[[11,12],[21,22],[31,32]]

#pattern-2

# mylist = []
# for i in range(1, 4):
#     for j in range(1, 3):
#         mylist.append(i * 10 + j)
# print(mylist)
# [11, 12, 21, 22, 31, 32]

mylist = [i * 10 + j for i in range(1, 4) for j in range(1, 3)]
print(mylist)
#[11,12,21,22,31,32]

mylist = [[i * 10 + j for j in range (1,3)] for i in range (1, 4)]
print(mylist)
#[[11,12],[21,22],[31,32]]