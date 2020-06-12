#encoding:utf-8

def test_func():
    print("call test_func")

test_func()

def test_func2(num_1, num_2, oprn=1):
    if oprn == 1:
        print("足し算開始")
        print(num_1 + num_2)
    
    elif oprn == 2:
        print("引き算開始")
        print(num_1 - num_2)
    
    elif oprn == 3:
        print("掛け算開始")
        print(num_1 * num_2)
    
    elif oprn == 4:
        print("割り算開始")
        print(num_1 / num_2)
    
    else:
        print("不明なオペレーション指定です")

test_func2(100, 10, 2)


#関数
def test_func():
    print("call test_func")

class TestClass:
    #メソッド
    def test_method():
        print("call test_method")
#モジュール内にdefで定義されているものが関数。class内にdefで定義されているのがメソッド（クラスがインスタンスかされてメソッドとなる。）