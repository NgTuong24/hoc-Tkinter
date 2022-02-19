from tkinter import *
win = Tk()
win.title("Hello W")

#kich thuoc cua so
# win.configure(width = 500, height = 600)
# win.geometry('300x500+50+50')

#kich thuoc man hinh may tinh
scrW = win.winfo_screenwidth()
scrH = win.winfo_screenheight()

win.geometry('300x500+%d+%d' %(scrW/2-200, scrH/2-300))
win.configure(bg = '#ffff7f')

# khong cho thay doi kich thuoc
win.resizable(width = False, height = False)
win.mainloop()