def samplefunc():
    print("This is sample")
    return 123 #returnの後には"戻り値"。returnおよび戻り値はあってもなくても良い

samplefunc() #①samplefunc関数を実行
samplefunc() #②6行目のsamplefunc関数を実行
val = samplefunc() #③
#print(val) #returnが無いのでNoneを返す？ print関数：def内のreturnを返す



def myfunc(name, age):
    print("Name:" + str(name) + ", Age:" + str(age))

myfunc("Yamada", 30)
myfunc("Saito", 35)