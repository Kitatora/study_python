#coding:utf-8
import tkinter as tk

def click(event):
    #クリックされたときにそこに描画する
    #円もしくは楕円を描く。(xn - yn): xはウィンドウからの座標。yはxを始点とした円周上の点の位置。1:左、2:上、3:右、4:下。event.x:クリックされたx座標。eventは4列目で定義された変数なので使える。」
    canvas.create_oval(event.x - 20, event.y - 20, event.x + 20, event.y + 20, fill = "red", width = 0) #ここでのwidthは線の幅
#ウィンドウを描く
root = tk.Tk()
root.geometry("600x400")

#Canvasを置く。変数canvasは他の変数名でも可能
canvas = tk.Canvas(root, width = 600, height = 400, bg="white")
canvas.place(x = 0, y = 0) #ウィンドウの上、キャンバスが重なった状態になる

canvas.bind("<Button-2>", click) #Macでbutton-1はシングルフィンガー、button-2はダブルフィンガー

root.mainloop()