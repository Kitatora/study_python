# coding:utf-8
import tkinter as tk

#縁をリストで用意する
balls = [
    {"x" : 400, "y" : 300, "dx" : 1, "dy" : 1, "color" : "red"},
    {"x" : 200, "y" : 100, "dx" : -1, "dy" : 1, "color" : "green"},
    {"x" : 300, "y" : 100, "dx" : -2, "dy" : 2, "color" : "purple"},
    {"x" : 100, "y" : 200, "dx" : 1, "dy" : -1, "color" : "blue"}
]

def move():
    global balls
    for b in balls:
        #既存の円を消す
        canvas.create_oval(b["x"] - 20 , b["y"] -20, b["x"] + 20, b["y"] + 20, fill = "white", width = 0)
        #x座標を動かす
        b["x"] = b["x"] + b["dx"]
        #y座標を動かす
        b["y"] = b["y"] + b["dy"]
        #次の位置に円を描く
        canvas.create_oval(b["x"] - 20, b["y"] - 20, b["x"] + 20, b["y"] + 20, fill = b["color"], width = 0)
        #端を超えていたら反対向きにする
        if b["x"]>= canvas.winfo_width():
            b["dx"] = -2 #マイナス座標、つまり左に移動
        if b["x"]<= 0:
            b["dx"] = 2
        #y軸についても同様に定義
        if b["y"]>= canvas.winfo_height():
            b["dy"] = -2 #マイナス座標、つまり左に移動
        if b["y"] <= 0:
            b["dy"] = 2
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