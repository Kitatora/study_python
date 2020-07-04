#encoding:utf-8
"""
持ち家vs賃貸　特定期間における総支出比較ツール
"""
import tkinter as tk

Class App(Frame): #ウィジェットの位置をgridで配置
    def __init__(self, master = None): 
        super().__init__(master, padx = 10, pady = 10)
        self.pack()

        #最初とリセットを押した時に表示する文字列
        self.var1 = StringVar()
        self.var1.set(self.initial)
        self.var1.set(self.initial)

        self.lab1 = Label(self, text)


