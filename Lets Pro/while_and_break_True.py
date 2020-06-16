#encoding:utf-8
num = 0
while True: #ブール値Trueで有る限り繰り返す。下は真のため、延々繰り返す
    print("num = " + str(num))
    num += 1
    if num >= 2:
        break

print("End")


#sample-2
print("Start")

while True:
    print("数値を入力すると 5 倍した値を表示します")
    print("終了する場合は -1 を入力してください")
    num = int(input("> "))
    if num == -1:
        break
    print("num = " + str(num) + ", num *  = " + str(num * 5) + "¥n")

print("End")