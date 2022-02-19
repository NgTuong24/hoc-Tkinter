from tkinter import *
win = Tk()
# Label(win, text="Hello World", bg = "red", fg = "blue").pack(side = BOTTOM, ipadx = 100, ipady = 100, padx=50, pady=50)
#           vitri
#           ipad x y chữ cách viền màu nền theo truc x100, y100
#           pad x y  viền màu nền cách biên 50    50
Label(win, text="Hello World", bg = "red", fg = "blue").pack(fill = X, ipady=50)
win.mainloop()