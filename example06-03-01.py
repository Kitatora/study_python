# coding:utf-8
import tkinter as tk

root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム") #ウィンドウを作る

labell = tk.Label(root, text="数を入力してください") #文章を入れる
labell.place(x = 20, y = 20) #変数の入力欄を動かす

editbox1 = tk.Entry(width =4) #テキスト入力欄を作る
editbox1.place(x = 150, y = 20)

root.mainloop() #ウィンドウを表示する
