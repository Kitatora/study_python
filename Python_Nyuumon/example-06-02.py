#coding:utf-8:
import tkinter as tk
#tkinter: GUIツールキット

root = tk.Tk() #ウィンドウを作成。変数名rootはなんでも良い
root.geometry("400x150") #geometry：ウィンドウサイズの変更
root.title("数あてゲーム") #title：ウィンドウの名称を変更
root.mainloop() #ウィンドウを表示する　☆root.やりたい操作()
#上記2行はウィンドウを表示する際の決まり文句！