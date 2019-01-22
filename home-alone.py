import nmap
import tkinter
from tkinter import *
from PIL import Image, ImageTk

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("Am I Home Alone?")

        self.label = Label(master, text="This is the app interface")

        # im_temp = Image.open("kevinscared.png")
        # im_temp = im_temp.resize((150, 250), Image.ANTIALIAS)

        self.photo = PhotoImage(file="kevinscared.png")
        self.panel = Label(root, image=self.photo)
        self.panel.photo = self.photo

        self.greet_button = Button(master, text="Greet", command=self.greet)
        # self.close_button = Button(master, text="Close", command=master.quit)

        self.label.grid(columnspan=2, sticky=W)
        self.greet_button.grid(row=1)
        self.panel.grid(row=1, column=1)

    def greet(self):
        print("Greetings!")




root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()


            # nm = nmap.PortScanner()
            #
            # my_scan = nm.scan(hosts='192.168.1.0/24', arguments='-O')
            #
            # print(my_scan)
