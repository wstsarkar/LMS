from tkinter import *


class LoginFrame(Frame):

    def __init__(self, master, controller):
        """ Initialize the Frame. """

        super(LoginFrame, self).__init__(master)
        self.master = master
        self.controller = controller

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create login ui that do nothing. """

        self.user_check_btn = Checkbutton(self, text="Employee Login")
        self.user_check_btn.grid()

        self.user_name_lbl = Label(self, text="User Name")
        self.user_name_lbl.grid()

        self.user_name_entry = Entry(self)
        self.user_name_entry.grid()

        self.user_name_lbl = Label(self, text="Password")
        self.user_name_lbl.grid()

        self.password_entry = Entry(self)
        self.password_entry.grid()

        self.login_btn = Button(self, text="Login ")
        self.login_btn.grid()
        self.login_btn.bind('<Button-1>', self.login)

        self.message_lbl = Label(self, text="")
        self.message_lbl.grid()

    def login(self, event):
        self.message_lbl.config(text="Success")
        self.controller.viewStudentForm()
