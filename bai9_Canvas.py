from tkinter import *
win = Tk()
# tao 1 doi tuong nao do
can1 = Canvas(win, width = 150, height= 150, bg = 'red')
can2 = Canvas(win, width = 150, height= 150, bg = 'blue')
# arrow
# arrowshape
can1.create_line(10,10,100,100,fill = 'black', width=10,arrow = 'last', arrowshape=(20,50,100))

can1.grid(row = 0, column=0)
can2.grid(row = 0, column=1)
win.mainloop()