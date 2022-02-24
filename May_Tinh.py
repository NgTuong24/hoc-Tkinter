from tkinter import *
import tkinter.ttk as exTk
import math
class MayTinh(Frame):
    def add(obj, n):
        if obj.s == "0":
            obj.s = ""
        obj.s += n
        obj.out_label.config(text=obj.s)
        obj.hthi_label.config(text=f"Ket qua la {obj.ss}")
    def add2(obj, n):
        if obj.s == "":
            obj.s = obj.ss
        if obj.s[-1] == '(' and n !='-':
            pass
        elif obj.s[-1] == '(' and n !='-':
            obj.s += n
            obj.out_label.config(text=obj.s)
            obj.hthi_label.config(text=f"Ket qua la {obj.ss}")
        else:
            if obj.s[-1] in ['-', '*'] and obj.s[-2] in ['*', '/', '(']:
                obj.out_label.config(text=obj.s)
            else:
                if obj.s[-1] in ['*', '/'] and n == '-':
                    pass
                else:
                    if obj.s[-1] in ['+', '-', '*', '/']:
                        obj.s = obj.s[:-1]

                obj.s += n
                obj.out_label.config(text=obj.s)
                obj.hthi_label.config(text=f"Ket qua la {obj.ss}")
    def ngtrai(obj, n):
        if obj.s == "0":
            obj.s = ""
        if len(obj.s) == 0:
            obj.s += n
        elif obj.s[-1].isalnum() or obj.s[-1] == ')' or obj.s[-1]=='.':
            obj.s += '*' + n
        else:
            obj.s += n
        obj.out_label.config(text=obj.s)
    def ngphai(obj, n):
        if len(obj.s) == 0:
            obj.out_label.config(text=obj.ss)
        else:
            if obj.s[-1].isalnum() and obj.s.count('(') > obj.s.count(')'):
                obj.s += n
            else:
                pass
            obj.out_label.config(text=obj.s)
    def sqr(obj, n):
        if obj.s == "0":
            obj.s = n
        elif obj.s[-1].isalnum() or obj.s[-1] == ')':
            obj.s += '*' + n
        else:
            pass
        obj.out_label.config(text=obj.s)
    def decimal(obj, n):
        if obj.s == '0':
            obj.s += '.'
        else:
            temp = len(obj.s)-1
            while obj.s[temp] not in ['+', '-', '*', '/'] and temp >= 0:
                temp -= 1
            if obj.s[temp].count('.') == 0:
                obj.s += '.'
        obj.out_label.config(text=obj.s)
    def result(obj):
        if obj.s[-1] == obj.s[-2] == '*':
            obj.tinh()
        if obj.s[-1] in ['+', '-', '*', '/' , '(', '.']:
            pass
        else:
            obj.tinh()
    def backspace(obj):
        if obj.s == "":
            obj.s = obj.ss
        obj.s = obj.s[:-1]
        if len(obj.s) == 0:
            obj.s = '0'
        obj.out_label.config(text=obj.s)
        obj.hthi_label.config(text=f"Ket qua la {obj.ss}")
    def CA(obj):
        obj.hthi_label.config(text=f"Ket qua la {obj.ss}")
        obj.s = "0"
        obj.out_label.config(text="0")
    def dongngoac(obj):
        while obj.s.count("(") > obj.s.count(")"):
            obj.s += ')'
    def xuly(obj):
        obj.dongngoac()
        obj.x = obj.s
        kq = ""
        i = 0
        while i < len(obj.x):
            if obj.x[i] == '^':
                kq = kq[:-1]
                kq += f"pow({obj.x[i-1]}, 2)"
            elif obj.x[i] == 'v':
                temp = i+1
                i += 1
                while obj.x[i] != ')' :
                    i += 1
                kq += f"math.sqrt{obj.x[temp:i+1]}"
            elif obj.x[i] == "%":
                kq +='/100'
            else:
                kq += obj.x[i]
            i += 1
        return kq
    def tinh(obj):
        d = obj.xuly()
        obj.hthi_label.config(text=f"{obj.s} = ")
        try:
            x = str(eval(d))
            obj.s = str(eval(d))
            obj.out_label.config(text=obj.s)
            obj.ss = obj.s
            obj.s = ""
        except :
            obj.s = 'ERROR'
            obj.out_label.config(text=obj.s)
            obj.s = ""


    def placeG(obj, el):
        objW = obj.winfo_width()
        objH = obj.winfo_height()

        obj.hthi_label.place(width=objW -30, height=30, x=10, y=0)
        obj.out_label.place(width=objW - 30, height=60, x=10, y=25)

        obj.ngTrai_btn.place(width=85, height=30, x=10, y=100)
        obj.ngPhai_btn.place(width=85, height=30, x=105, y=100)
        obj.del_btn.place(width=85, height=30, x=200, y=100)
        obj.ca_btn.place(width=85, height=30, x=295, y=100)

        obj.square_btn.place(width=85, height=30, x=10, y=140)
        obj.can_btn.place(width=85, height=30, x=105, y=140)
        obj.phanTram_btn.place(width=85, height=30, x=200, y=140)
        obj.div_btn.place(width=85, height=30, x=295, y=140)

        obj.n7btn.place(width=85, height=30, x=10, y=180)
        obj.n8btn.place(width=85, height=30, x=105, y=180)
        obj.n9btn.place(width=85, height=30, x=200, y=180)
        obj.mul_btn.place(width=85, height=30, x=295, y=180)

        obj.n4btn.place(width=85, height=30, x=10, y=220)
        obj.n5btn.place(width=85, height=30, x=105, y=220)
        obj.n6btn.place(width=85, height=30, x=200, y=220)
        obj.sub_btn.place(width=85, height=30, x=295, y=220)

        obj.n1btn.place(width=85, height=30, x=10, y=260)
        obj.n2btn.place(width=85, height=30, x=105, y=260)
        obj.n3btn.place(width=85, height=30, x=200, y=260)
        obj.sum_btn.place(width=85, height=30, x=295, y=260)

        obj.n0btn.place(width=85, height=30, x=10, y=300)
        obj.decimal_btn.place(width=85, height=30, x=105, y=300)
        obj.cal_btn.place(width=180, height=30, x=200, y=300)

    def __init__(obj, win):
        super().__init__(win)
        obj.s = "0"
        obj.ss =""
        obj.x = ""
        obj.hthi_label = exTk.Label(obj, text=obj.ss, anchor=E, font="Times 10")
        obj.out_label = exTk.Label(obj, text=obj.s, anchor=E, font="Times 10")

        obj.ngTrai_btn = Button(obj, text="(", bg="gray", font="Times 15", command = lambda :obj.ngtrai("("))
        obj.ngPhai_btn = Button(obj, text=")", bg="gray", font="Times 15", command = lambda :obj.ngphai(")"))
        obj.del_btn = Button(obj, text="Del", bg = "red", fg="white", font="Times 15",command=obj.backspace)
        obj.ca_btn = Button(obj, text="CA", bg ="red", fg="white", font="Times 15", command=obj.CA)

        obj.square_btn = Button(obj, text="^x", bg="gray", font="Times 15", command = lambda :obj.add2("**"))
        obj.can_btn = Button(obj, text="v", bg="gray", font="Times 15", command = lambda :obj.sqr("v("))
        obj.phanTram_btn = Button(obj, text="%",bg="gray", font="Times 15", command = lambda :obj.add2("%"))
        obj.div_btn = Button(obj, text="/", bg="black", fg="white", font="Times 15 bold", command = lambda :obj.add2("/"))

        obj.n7btn = Button(obj, text="7", font="Times 15", command = lambda :obj.add("7"))
        obj.n8btn = Button(obj, text="8", font="Times 15", command = lambda :obj.add("8"))
        obj.n9btn = Button(obj, text="9", font="Times 15", command = lambda :obj.add("9"))
        obj.mul_btn = Button(obj, text="*", bg="black", fg="white", font="Times 15 bold", command = lambda :obj.add2("*"))

        obj.n4btn = Button(obj, text="4", font="Times 15", command = lambda :obj.add("4"))
        obj.n5btn = Button(obj, text="5", font="Times 15", command = lambda :obj.add("5"))
        obj.n6btn = Button(obj, text="6", font="Times 15", command = lambda :obj.add("6"))
        obj.sub_btn = Button(obj, text="-", bg="black", fg="white", font="Times 15 bold", command = lambda :obj.add2("-"))

        obj.n1btn = Button(obj, text="1", font="Times 15", command = lambda :obj.add("1"))
        obj.n2btn = Button(obj, text="2", font="Times 15", command = lambda :obj.add("2"))
        obj.n3btn = Button(obj, text="3", font="Times 15", command = lambda :obj.add("3"))
        obj.sum_btn = Button(obj, text="+", bg="black", fg="white", font="Times 15 bold", command = lambda :obj.add2("+"))

        obj.n0btn = Button(obj, text="0", font="Times 15", command = lambda :obj.add("0"))
        obj.decimal_btn = Button(obj, text=".", font="Times 15", command = lambda :obj.decimal('.'))
        obj.cal_btn = Button(obj, text="=", bg="blue", fg="white", font="Times 15 bold", command=obj.result)

        obj.bind("<Configure>", obj.placeG)
win = Tk()
win.geometry('390x360')
win.resizable(width=False, height=False)
mt = MayTinh(win)
mt.place(relwidth=1, relheight=1)
win.mainloop()