# coding:utf-8
import tkinter as tk
import tkinter.messagebox as tmsg
import random

#ボタンがクリックされたときの処理
def ButtonClick():
    b = editbox1.get() #テキスト入力欄に入力された文字列を取得。変数.getメソッドを使用

    #Lesson 5-4のプログラム。4桁の数字かどうかを判定
    #4桁の数字かどうかを判断する
    isok = False
    if len(b)!= 4:
        tmsg.showerror("エラー","4桁の数字を入れてください")
    else:
        kazuok = True
        for i in range(4):
            if (b[i] < "0") or (b[i] > "9"):
                tmsg.showerror("エラー", "数字ではありません")
                kazuok = False
                break
        if kazuok:
            isok = True
    
    if isok:
    #4桁の数字だった場合。ヒットを判定
        hit = 0
        for i in range(4):
            if a[i] == int(b[i]):
                hit = hit +1
        #ブローを判定
        blow = 0
        for j in range(4):
            for i in range(4):
                if (int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                    blow = blow + 1
                    break
    #ヒットが4なら正解となり、終了
        if hit == 4:
            tmsg.showinfo("正解！", "おめでとうございます！")
            #終了
            root.destroy()
        else: #ヒット数とブロー数を表示。
            rirekibox.insert(tk.END, b + "   /H:" + str(hit) + " B:" + str(blow) + "\n")#ウィンドウ向けに新たに調整した部分

#メインのプログラム
#予めランダムな4つの数字を設定
a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]

#ウィンドウを作る
root = tk.Tk()
root.geometry("600x400")
root.title("数当てゲーム") #ウィンドウを作る

#履歴表示のテキストボックスを作る
rirekibox = tk.Text(root, font = ("Meiryo UI", 14))
rirekibox.place(x=400, y=0, width=200, height=400)

#ラベルを作る
label1 = tk.Label(root, text="数を入力してください", font=("Meiryo UI", 14)) #文章を入れる
label1.place(x = 20, y = 20) #変数の入力欄を動かす

#テキストボックス（プレイヤーの入力欄）を作る
editbox1 = tk.Entry(width =4, font = ("Meiryo UI", 28)) #テキスト入力欄を作る
editbox1.place(x = 160, y = 20)

#ボタンを作る
button1 = tk.Button(root, text = "チェック", font = ("Meiryo UI", 14), command = ButtonClick)
button1.place(x = 240, y = 20)

#ウィンドウを表示する
root.mainloop() #ウィンドウを表示する
