from tkinter import *
win = Tk()
'''
Label(win, text = "Doan van 1", font = 'Times 20', bg = 'red').grid(row = 0, column = 0, sticky=E)
Label(win, text = "Doan van 2", font = 'Times 25', bg = 'blue').grid(row = 1, column = 0)
Label(win, text = "Doan van 3", font = 'Times 30', bg = 'orange').grid(row = 0, column= 1, sticky=W)
Label(win, text = "Doan van 4", font = 'Times 35', bg = 'green').grid(row = 1, column=1, sticky=W)
Label(win, text = "Doan van 5", font = 'Times 40', bg = 'brown').grid(row = 2, columnspan=2)


# sticky N, E, S, W, NE, NW, SE, SW..
# .gird(row = , column = )
'''
# kich thuoc o label / co dinh
# Label(win, text = " Doan van", bg = 'red').place(width = 70, height = 100)
# kich thuoc theo ti le  .5 ~ 50%
# Label(win, text = " Doan van", bg = 'red').place(relwidth=.5, relheight=.5, x = 50, y = 50)

Label(win, text = " Doan van", bg = 'red').place(relwidth=.5, relheight=.5, relx = .1, rely = .1)

win.mainloop()