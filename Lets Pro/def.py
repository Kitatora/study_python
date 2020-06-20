def samplefunc():
    print("This is sample")

samplefunc()
samplefunc()
val = samplefunc()
print(val) #引数が無いのでNoneを返す？



def myfunc(name, age):
    print("Name:" + str(name) + ", Age:" + str(age))

myfunc("Yamada", 30)
myfunc("Saito", 35)