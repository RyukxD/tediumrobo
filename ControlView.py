"""
import Control
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createlabel(master)
        self.control = Control.Control(10)
        self.mylabel = Label()
        self.mylabel.pack()
        self.contents = StringVar()
        self.contents.set(self.control.refresh())
        self.mylabel["textvariable"] = self.contents


    def createlabel(self, master):
        self.robot = Button(self, text="Create a robot", command=self.createrobot).grid(row = 1, column = 0)
        #self.hi_there = Button(self, text="Refresh", command=self.refresh).grid(row = 1, column = 1)
        self.attack_button = Button(self, text=" attack a robot", command=self.attack).grid(row = 1, column = 1)
        self.quit = Button(self, text="Esci", fg="red", command=master.destroy).grid(row = 1, column = 2)

    def refresh(self):
        self.contents.set(self.control.refresh())

    def createrobot(self):
        self.top = Toplevel(self)
        self.labelname = Label(self.top, text="Name").grid(row=0)
        self.labelweap = Label(self.top, text="Weap").grid(row=1)
        self.name = Entry(self.top)
        self.weap = Entry(self.top)
        self.name.grid(row=0, column=1)
        self.weap.grid(row=1, column=1)
        self.check = Button(self.top, text="Crea", command=self.create).grid(row=2, column=1)


    def create(self):
        self.control.createrobot(self.name.get(), self.weap.get())
        self.refresh()
        self.top.destroy()

    def attack(self):
        self.control.attack(self.name.get(), self.weap.get())
        self.refresh()
        self.top.destroy()

    def start(self):
        test = Tk()
        app = Application(test)
        app.mainloop()



"""
import Control
from tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createlabel(master)
        self.control = Control.Control(10)
        self.mylabel = Label()
        self.mylabel.pack()
        self.contents = StringVar()
        self.contents.set(self.control.refresh())
        self.mylabel["textvariable"] = self.contents


    def createlabel(self, master):
        self.robot = Button(self, text="Crea un robot", command=lambda: self.entry(0)).grid(row = 1, column = 0)
        #self.hi_there = Button(self, text="Refresh", command=self.refresh).grid(row = 1, column = 1)
        self.attack_button = Button(self, text=" attacca un robot", command=lambda: self.entry(1)).grid(row = 1, column = 1)
        self.quit = Button(self, text="Esci", fg="red", command=master.destroy).grid(row = 1, column = 2)

    def refresh(self):
        self.contents.set(self.control.refresh())

    def entry(self, case):
        self.top = Toplevel(self)
        if case is 0:
            self.labelname = Label(self.top, text="Nome").grid(row=0)
            self.labelweap = Label(self.top, text="Arma").grid(row=1)
        else:
            self.labelweap = Label(self.top, text="Robot2").grid(row=1)
            self.labelname = Label(self.top, text="Robot1").grid(row=0)
        self.name = Entry(self.top)
        self.weap = Entry(self.top)
        self.name.grid(row=0, column=1)
        self.weap.grid(row=1, column=1)
        self.check = Button(self.top, text="Ok", command=lambda: self.action(case)).grid(row=2, column=1)


    def action(self, action):
        if action is 0:
            self.control.createrobot(self.name.get(), self.weap.get())
        else:
            self.control.attack(self.name.get(), self.weap.get())
        self.refresh()
        self.top.destroy()


    def start(self):
        test = Tk()
        app = Application(test)
        app.mainloop()
