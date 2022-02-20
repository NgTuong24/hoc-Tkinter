from tkinter import *
import tkinter.ttk as exTk
def chon():
    lbHienthi['text'] = "Bạn đã chọn: " + cmb1.get()
    # lbHienthi.config(text = "Đã thay đổi")
    # lbHienthi.configure(text="thay doi")
win = Tk()
cmb1 = exTk.Combobox(win, width=30, font = 'Times 30', state='readonly')
cmb1['values'] = ('ntu', 'co khi', 'dien tu')
cmb1.current(0)
btnChon = Button(win, text = "chọn", font = 'Times 21', command=chon)
lbHienthi = Label(win, text = 'Chưa chọn')

cmb1.grid(row=0, column=0)
btnChon.grid(row = 0, column =1, padx=10)
lbHienthi.grid(row = 1, column= 0)
win.mainloop()

'''
current(0) mặc định xh giá trị đầu tiên
state = "readonly"  ko cho thay doi values cua combobox
'''

