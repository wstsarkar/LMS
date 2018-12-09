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

    def create_widgets(self):
        for widget in self.winfo_children():
            widget.destroy()

        self.lib_name = Label(self, text="Wecome to " + self.container.library.getNeme())
        self.lib_name.grid(row=0, column=0, columnspan=2, sticky=EW)

        self.lib_address = Label(self, text="Address " + self.container.library.getAddress())
        self.lib_address.grid(row=1, column=0, columnspan=2, rowspan=2, sticky=EW)

        self.chk_state = BooleanVar()
        self.chk_state.set(True)
        self.is_employee_ck_btn = Checkbutton(self, text="Employee Login", var=self.chk_state)
        self.is_employee_ck_btn.grid(row=5, column=1, sticky=W)



        self.user_name = Label(self, text="User Name")
        self.user_name.grid(row=6, column=0, sticky=E)

        self.user_name_entry = Entry(self)
        self.user_name_entry.grid(row=6, column=1)

        self.password = Label(self, text="Password")
        self.password.grid(row=7, column=0, sticky=E)

        self.password_entry = Entry(self)
        self.password_entry.grid(row=7, column=1)

        self.login_btn = Button(self, text="Login")
        self.login_btn .grid(row=8, column=0, sticky=E)
        self.login_btn .bind('<Button-1>', self.login)

        self.cancel_btn = Button(self, text="Clear")
        self.cancel_btn.grid(row=8, column=1, sticky=E)
        self.cancel_btn.bind('<Button-1>', self.clear)

        self.message_lbl = Label(self, text="")
        self.message_lbl.grid(row=9, column=1, sticky=W)


    def login(self, event):
        print(self.chk_state.get())
        if self.chk_state.get():
            for user in self.container.library.getAllUser():
                if user.getUserName().upper() == self.user_name_entry.get().upper() and user.getPassword() == self.password_entry.get():
                    self.clearForm()
                    self.container.viewMenu(isEmp=True)
            self.message_lbl.config(text="Login Failed")
        else:
            for student in self.container.library.getAllStudent():
                if student.getUserName().upper() == self.user_name_entry.get().upper() and student.getPassword() == self.password_entry.get():
                    self.clearForm()
                    self.container.viewMenu(isEmp=False)
            self.message_lbl.config(text="Login Failed")


    def clear(self,event):
        self.clearForm()

    def clearForm(self):
        self.user_name_entry.delete(0, 'end')
        self.password_entry.delete(0, 'end')
        self.user_name_entry.focus()


    def getMainGeometry(self):
        return "280x200"
    def getMainTitle(self):
        return "Login Form"
