#coding:utf-8
import tkinter as tk

#円の座標
x = 300
y = 200

def click(event):
    global x, y
    #クリックされたときにそこに描画する
    #円もしくは楕円を描く。
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "white", width = 0) #ここでのwidthは線の幅
    x = event.x
    y = event.y
    canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill = "red", width = 0)
#ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

#Canvasを置く。変数canvasは他の変数名でも可能
canvas = tk.Canvas(root, width = 600, height = 400, bg="white")
canvas.place(x = 0, y = 0) #ウィンドウの上、キャンバスが重なった状態になる

canvas.bind("<Button-1>", click) #Macでbutton-1はシングルフィンガー、button-2はダブルフィンガー

root.mainloop()