# coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg

#ボタンがクリックされたときの処理
def ButtonClick():
    tmsg.showinfo("テスト", "クリックされた")
root = tk.Tk()
root.geometry("400x150")
root.title("数当てゲーム") #ウィンドウを作る

label1 = tk.Label(root, text="数を入力してください", font=("Meiryo UI", 14)) #文章を入れる
label1.place(x = 20, y = 20) #変数の入力欄を動かす

editbox1 = tk.Entry(width =4, font = ("Meiryo UI", 28)) #テキスト入力欄を作る
editbox1.place(x = 160, y = 20)

button1 = tk.Button(root, text = "チェック", font = ("Meiryo UI", 14), command = ButtonClick)
button1.place(x = 240, y = 20)

root.mainloop() #ウィンドウを表示する
