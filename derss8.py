import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_916=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_916["font"] = ft
        GLabel_916["fg"] = "#333333"
        GLabel_916["justify"] = "center"
        GLabel_916["text"] = "KULLANICI GİRİŞİ"
        GLabel_916.place(x=220,y=60,width=132,height=82)

        GButton_140=tk.Button(root)
        GButton_140["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_140["font"] = ft
        GButton_140["fg"] = "#000000"
        GButton_140["justify"] = "center"
        GButton_140["text"] = "Button"
        GButton_140.place(x=150,y=240,width=70,height=25)
        GButton_140["command"] = self.GButton_140_command

        GLineEdit_360=tk.Entry(root)
        GLineEdit_360["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_360["font"] = ft
        GLineEdit_360["fg"] = "#333333"
        GLineEdit_360["justify"] = "center"
        GLineEdit_360["text"] = "Entry"
        GLineEdit_360.place(x=230,y=120,width=113,height=34)

        GLabel_768=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "kullanıcı adı"
        GLabel_768.place(x=110,y=110,width=115,height=56)

        GLabel_537=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_537["font"] = ft
        GLabel_537["fg"] = "#333333"
        GLabel_537["justify"] = "center"
        GLabel_537["text"] = "şifre"
        GLabel_537.place(x=110,y=180,width=97,height=30)

        GLineEdit_573=tk.Entry(root)
        GLineEdit_573["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_573["font"] = ft
        GLineEdit_573["fg"] = "#333333"
        GLineEdit_573["justify"] = "center"
        GLineEdit_573["text"] = "2"
        GLineEdit_573.place(x=230,y=180,width=115,height=35)

    def GButton_140_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
