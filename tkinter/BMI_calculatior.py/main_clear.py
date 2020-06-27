#encoding:utf-8

from tkinter import *
class App(Frame):

    def __init__(self, master=None):
        super().__init__(master, padx=10, pady=10)
        self.pack()

        self.initial = "身長と体重を入力して\nボタンを押して下さい\n"
        self.var1 = StringVar()
        self.var1.set(self.initial)

        self.lab1 = Label(self, text="BMI ボディマス指数計算")
        self.lab1.grid(row=0, column=0, columnspan=4)

        self.lab2 = Label(self, text="身長")
        self.lab2.grid(row=1, column=0)

        self.ent1 = Entry(self, justify=RIGHT)
        self.ent1.grid(row=1, column=1, columnspan=2)
        self.ent1.focus()
        self.ent1.bind("<Return>", self.calc)

        self.lab4 = Label(self, text="cm")
        self.lab4.grid(row=1, column=3)

        self.lab3 = Label(self, text="体重")
        self.lab3.grid(row=2, column=0)

        self.ent2 = Entry(self, justify=RIGHT)
        self.ent2.grid(row=2, column=1, columnspan=2)
        self.ent2.bind("<Return>", self.calc)

        self.lab5 = Label(self, text="kg")
        self.lab5.grid(row=2, column=3)

        self.btn1 = Button(self, text="計算", command=self.calc)
        self.btn1.grid(row=3, column=1)

        self.btn2 = Button(self, text="リセット", command=self.clear)
        self.btn2.grid(row=3, column=2)

        self.lab6 = Label(self, textvariable=self.var1)
        self.lab6.grid(row=4, column=0, columnspan=4)

        self.img = PhotoImage(file="img/1.png")

        self.lab7 = Label(self, image=self.img)
        self.lab7.grid(row=5, column=0, columnspan=4)

    def calc(self, _=None):
        try:
            height = float(self.ent1.get())
            weight = float(self.ent2.get())
            bmi = round(weight / ((height / 100) * (height / 100)), 2)
            right_weight = round(((height / 100) * (height / 100)) * 22, 2)

            if bmi < 18.5:
                result = "低体重"
                self.img["file"] = "img/2.png"
                self.lab7["image"] = self.img

            elif 18.5 <= bmi < 25:
                result = "普通体重"
                self.img["file"] = "img/3.png"
                self.lab7["image"] = self.img

            elif 25 <= bmi < 30:
                result = "肥満（１度）"
                self.img["file"] = "img/4.png"
                self.lab7["image"] = self.img

            elif 30 <= bmi < 35:
                result = "肥満（２度）"
                self.img["file"] = "img/4.png"
                self.lab7["image"] = self.img

            elif 35 <= bmi < 40:
                result = "肥満（３度）高度肥満"
                self.img["file"] = "img/4.png"
                self.lab7["image"] = self.img

            elif 40 <= bmi:
                result = "肥満（４度）高度肥満"
                self.img["file"] = "img/4.png"
                self.lab7["image"] = self.img

            ans = f"あなたのBMIは{bmi}です。\n{result}です。\n適正体重は{right_weight}kgです。"

            self.var1.set(ans)

        except ValueError:
            self.var1.set("ValueError\n半角の数字を入力して下さい\n")
        except ZeroDivisionError:
            self.var1.set("ZeroDivisionError\n0で割れません\n")

    def clear(self):
        self.img["file"] = "img/1.png"
        self.lab7["image"] = self.img
        self.var1.set(self.initial)
        self.ent1.delete(0, END)
        self.ent2.delete(0, END)
        self.ent1.focus()


root = Tk()
root.title("BMI")
root.option_add("*Font", "メイリオ 12")
app = App(master=root)
root.mainloop()