from tkinter import *
#masaüstü uygulama tkinter

window = Tk()

window.title("MERHABA PYTHON GUİ")
lbl = Label(window, text="MERHABA")#ekranda göstermek için
lbl.grid(column=10,row=10)#ekranda göstermek için


window.mainloop()