from tkinter import *
import tkinter.ttk as exTk
import tkinter.scrolledtext as scllText

class monitor(Frame):
    # hàm placeGui pack(...) lên giao diện
    def placeGui(obj, e):
        # obj.update()
        if e.widget == obj:
        # objw = obj.winfo_width()
        # objh = obj.winfo_height()
            objw = e.width
            objh = e.height

            obj.sendBtn.place(height=25, width=50, x=objw - 50, y=10)
            obj.inputText.place(height=25, width=objw - 55, x=0, y=10)

            obj.outputText.place(height=objh - 105, width=objw-10, x=0, y=40)
            obj.houtputText.place(height=20, width=objw-20, x=0, y=objh -55)

            obj.clearBtn.place(height=25, width=80, x=objw - 85, y=objh - 30)
            obj.baudCbb.place(height=23, width=80, x=objw - 175, y=objh - 29)
            obj.baudCbb2.place(height=23, width=80, x=objw - 265, y=objh - 29)
            obj.autoscroll.place(height=25, width=80, x=10, y=objh - 29)
            obj.showtime.place(height=25, width=80, x=100, y=objh - 29)
    #win : cua so
    def __init__(obj, win):
        # mở rộng kế thừa của Frame
        super().__init__(win)
        obj.inputText = exTk.Entry(obj)

        #thanh trượt
        obj.houtputText = Scrollbar(obj, orient=HORIZONTAL)
        obj.outputText = scllText.ScrolledText(obj, wrap = 'none', xscrollcommand=obj.houtputText.set) # thanh trượt dọc
        obj.houtputText['command'] = obj.outputText.xview

        obj.sendBtn = exTk.Button(obj, text = "Send")
        obj.clearBtn = exTk.Button(obj, text="Clear output")
        obj.baudCbb = exTk.Combobox(obj)
        obj.baudCbb2 = exTk.Combobox(obj)
        obj.autoscroll = exTk.Checkbutton(obj, text = "Autoscroll")
        obj.showtime = exTk.Checkbutton(obj, text = "Show timestamp")

        win.bind("<Configure>", obj.placeGui)

win = Tk()
icon = Image("photo", file='venv/img.png.')
win.wm_iconphoto(True, icon)
win.geometry("500x500")
win.title("APP")
Monit = monitor(win)
Monit.place(relwidth=1, relheight=1)
win.mainloop()