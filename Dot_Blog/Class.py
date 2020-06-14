class NameCheck:
    
    #__init__関数(self, 第二引数)。ここでのselfはインスタンスに入力した引数を戻す効果
    #インスタンスに入った引数は__init__関数の第二引数に入ることに注意。
    def __init__(self, text):
        self.text = text #self.textをインスタンス変数と言う
        print(self.text)
        self.length = 0　#インスタンス変数lengthを宣言
        test = 10
    #インスタンス変数は同一クラス内で共有が可能

    def text_len(self):
        #len関数でシンプルに数えられる？
    # for i in self.text:
        #    self.length += 1
        self.length = len(self.text)
        print(test)
        return self.length
    
    def even_or_odd(self):
        if self.length % 2 == 0:
            return '偶数'
        else:
            return '奇数'

x1 = 'たろう'

# クラス『NameCheck』をインスタンス化
nc_ta = NameCheck(x1)
#NameCheckクラスの()に入った値を引数として__init__関数に返す
test = nc_ta.text_len()
print(test)
test2 = nc_ta.even_or_odd()
print(test2)

x2 = 'さぶろう'
nc_ta = NameCheck(x2)
test = nc_ta.text_len()
print(test)
test2 = nc_ta.even_or_odd()
print(test2)
#一度インスタンス化したら以降不要