#coding:utf-8
import tkinter as tk
class Ball:
    def __init__(self, x, y, dx, dy, color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color
    
    def move(self, canvas):
        #今の円を満たす
        self.erase(canvas)
        #X座標、y座標を動かす
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        #次の位置に円を描画する
        self.draw(canvas)
        #端を超えていたら反対向きにする
        if (self.x >= canvas.winfo_width()):
            self.dx = -1
        if (self.x <= 0):
            self.dx = 1
        if (self.y >= canvas.winfo_height()):
            self.dy = -1
        if (self.y <= 0):
            self.dy = 1
    
    def erase(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="white", width=0)

    def draw(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=self.color, width=0)

class Rectangle(Ball):
    def erase(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="white", width=0)
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=self.color, width=0)

class Triangle(Ball):
    def erase(self, canvas):
        canvas.create_polygon(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill="white", width=0)
    
    def draw(self, canvas):
        canvas.create_polygon(self.x - 20, self.y - 20, self.x + 20, self.y + 20, fill=self.color, width=0)

#円、四角形、三角形をまとめて用意する
balls = [
    Ball(400, 300, 1, 1, "red"),
    Rectangle(200, 100, -1, 1, "green"),
    Triangle(100, 200, 1, -1, "blue")
]
def loop():
    #動かす
    for b in balls:
        b.move(canvas)
    #もいう一回
    root.after(10, loop)

#ウィンドウを描く
root = tk.Tk()
root.geometry("800x600")

#Canvasを置く
canvas = tk.Canvas(root, width = 800, height = 600, bg="#fff")
canvas.place(x = 0, y = 0)

#タイマーをセット
root.after(10, loop)

root.mainloop()