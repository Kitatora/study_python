#encoding:utf-8

colorlist = ["Blue", "Red", "Green"]

print(colorlist)
print("オブジェクトの id = " + str(id(colorlist)))
print("¥n")

colorlist[1] = "White"
print(colorlist)
print("オブジェクトの id = " + str(id(colorlist)))