from tkinter import *
win = Tk()
def hienthi():
    print(entName.get())
    Label(win, text = entName.get() + '\n' + entPhone.get(), font = 'Times 40 bold').pack()

# input
entName = Entry(win, font = 'Times 40 bold')

entPhone = Entry(win, font = 'Times 40 bold')
btn = Button(win, text = 'enter', font = 'Times 40 bold', command=hienthi)

entName.pack()
entPhone.pack()
btn.pack()
entName.focus() # xh con trỏ chuột khi chạy ctrinh
win.mainloop()