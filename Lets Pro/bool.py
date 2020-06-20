#encoding:utf-8

print(bool("ABC"))
print(bool(0))
print(bool(0.00001))
print(bool(2j))
print(bool(100))
print(bool([10,20,30,40,50]))
print(bool(["A", "B", "C"]))
print(bool(""))

#オブジェクト0や""の時にFalseを返す。値、数字が"存在しない"場合にFalseを返す。虚数は真を返す