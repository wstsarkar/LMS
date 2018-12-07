from tkinter import *
from user import *
from student import *
from container import *


class LoginFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(LoginFrame, self).__init__(master)
        self.master = master
        self.container = container
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.chk_state = BooleanVar()

        self.is_employee_ck_btn = Checkbutton(self, text="Employee Login", var=self.chk_state)
        self.is_employee_ck_btn.grid()

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
        print(self.chk_state.get())
        if self.chk_state.get():
            for user in self.container.library.getAllUser():
                if user.getUserName() == self.user_name_entry.get() and user.getPassword() == self.password_entry.get():
                    self.container.viewStudentListFrame()
            self.message_lbl.config(text="Login Failed")
        else:
            for student in self.container.library.getAllStudent():
                if student.getUserName() == self.user_name_entry.get() and student.getPassword() == self.password_entry.get():
                    self.container.viewStudentListFrame()
            self.message_lbl.config(text="Login Failed")


    def getMainGeometry(self):
        return "200x400"
    def getMainTitle(self):
        return "Login Form"
