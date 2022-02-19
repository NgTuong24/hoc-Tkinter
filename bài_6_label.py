from tkinter import *
win = Tk()

# kich cuo cho cua so
w = win.winfo_screenwidth()
h = win.winfo_screenheight()
win.geometry('400x500+%d+%d' %(w/2-200, h/2-150))
win.resizable(width = False, height=False)
win.configure(bg = "#00f0ff")
#

lb1 = Label(win, text = "Hello 1 \nworld\nHI", bg = "red", fg="white",
            font="Oswald 20 bold", width=10, height=5,
            relief = "solid", borderwidth = 10, #duong bien
            anchor = CENTER,            # vtri NEWS
            padx = 10, pady=30,
            justify=LEFT)               #can le
lb2 = Label(win, text = "HI 2", bg = "blue", fg="white")


lb1.pack()
lb2.pack()
win.mainloop()