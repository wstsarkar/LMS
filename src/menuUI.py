from tkinter import *
from loginUI import *
from studentFormUI import *
from userFormUI import *
from studentListUI import *

class MenuFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(MenuFrame, self).__init__(master)
        self.master = master
        self.container = container
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.login_btn = Button(self, text="Student List")
        self.login_btn.grid()
        self.login_btn.bind('<Button-1>', self.login)

    def login(self, event):
        self.message_lbl.config(text="Login Failed")


    def getMainGeometry(self):
        return "200x400"
    def getMainTitle(self):
        return "Login Form"
