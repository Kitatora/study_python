#利用できるフォント一覧を取得する。
import tkinter as tk
for f in tk.Tk().call("font", "families"):
    print(f)

