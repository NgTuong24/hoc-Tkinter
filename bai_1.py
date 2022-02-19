from tkinter import *
import threading   #luồng

win = Tk("")
label1 = Label(win, text = "Ngoi Nha IoT left")
# dong goi len giao dien
label1.pack(side = LEFT)
label2 = Label(win, text = "Ngoi Nha IoT right")
label2.pack(side = RIGHT)

def setText():
    while(True):
        content = input()
        label1.config(text = content)  # sua
        # win.after(1000, setText)

# sau 1000s chay ham setText lai 1 lan
# win.after(1000, setText)
setTextThr = threading.Thread(target = setText)
setTextThr.start()

win.mainloop()
