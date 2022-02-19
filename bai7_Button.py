from tkinter import *
def creatButton():
    bt = Button(win, text="Submit: %d" %creatButton.count,
                font="times 10 bold",
                command=creatButton).grid(row=creatButton.count, column=0)

    lb = Label(win, text="Lable: %d" % creatButton.count,
                font="times 10 bold").grid(row=creatButton.count, column=1)
    creatButton.count += 1


win = Tk()
win.geometry("500x200+350+200")
win.resizable(width=False, height=False)

creatButton.count = 0
creatButton()

win.mainloop()