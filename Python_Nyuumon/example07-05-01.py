# coding:utf-8
import tkinter as tk

#円の座標
x = 400
y = 300
#移動量
dx = 1

def move():
    global x, y, dx
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "white", width = 0)
    #x座標を動かす
    x = x + dx
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "red", width = 0)
    #端を超えていたら反対向きにする
    if x>= canvas.winfo_width():
        dx = -1 #マイナス座標、つまり左に移動
    if x <= 0:
        dx = 1
    #再びタイマー
    root.after(10, move) #次も実行されるようにするため、再設定

#ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

#キャンバスを置く
canvas = tk.Canvas(root, width = 600, height = 400, bg = "white")
canvas.place(x = 0, y = 0)

#イベントを設定する
root.after(10, move)

root.mainloop()