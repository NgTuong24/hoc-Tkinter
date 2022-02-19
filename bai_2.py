from tkinter import *
def len():
    if lenBtn['bg'] == "red":
        lenBtn['bg'] = "black"
    else:
        lenBtn['bg'] = "red"
    print('len')
def xuong():
    print('xuong')
def trai():
    print('trai')
def phai():
    print('phai')

win = Tk()
fame1 = Frame(win)
fame1.pack()

fame2 = Frame(win)
fame2.pack()

fame3 = Frame(win)
fame3.pack()

lenBtn = Button(fame1, text = "len", command = len, bg="red", fg='white')
lenBtn.pack()

traiBtn = Button(fame2, text = "trai", command = trai, bg="green", fg='white')
traiBtn.pack(side = LEFT)

phaiBtn = Button(fame2, text = "phai", command = phai, bg="green", fg='white')
phaiBtn.pack(side = RIGHT)

xuongBtn = Button(fame3, text = "xuong", command = xuong, bg="red", fg='white')
xuongBtn.pack()

win.mainloop()