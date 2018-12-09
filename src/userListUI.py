

from tkinter import *
from user import *
from container import *


class UserListFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(UserListFrame, self).__init__(master)
        self.master = master
        self.container = container

        self.grid()

    def create_widgets(self):

        for widget in self.winfo_children():
            widget.destroy()


        self.back_btn = Button(self, text="Back")
        self.back_btn.grid(row=0, column=0, sticky=W)
        self.back_btn.bind('<Button-1>', self.back)

        self.logout_btn = Button(self, text="Logout")
        self.logout_btn.grid(row=0, column=5, sticky=E)
        self.logout_btn.bind('<Button-1>', self.logout)

        self.add_book_btn = Button(self, text="Add Employee")
        self.add_book_btn.grid(row=1, column=0, sticky=W)
        self.add_book_btn.bind('<Button-1>', self.gotoEmployeeForm)


        row = 2
        Label(self, text="Name").grid(row=row, column=0, sticky=EW)

        Label(self, text="User Name").grid(row=row, column=1, sticky=EW)

        Label(self, text="Address").grid(row=row, column=2, sticky=EW)

        Label(self, text="Phone No").grid(row=row, column=3, sticky=EW)

        Label(self, text="Action").grid(row=row, column=4, columnspan=2, sticky=EW)


        for user in self.container.library.getAllUser():

            row += 1

            Label(self, text=user.getNeme()).grid(row=row, column=0, sticky=W)

            Label(self, text=user.getUserName()).grid(row=row, column=1, sticky=W)

            Label(self, text=user.getAddress()).grid(row=row, column=2, sticky=W)

            Label(self, text=user.getPhoneNo()).grid(row=row, column=3, sticky=W)

            Button(self, text="Edit", command=lambda: self.deleteUser(user)).grid(row=row, column=4, sticky=W)

            Button(self, text="Delete", command=lambda: self.deleteUser(user)).grid(row=row, column=5, sticky=W)

    def deleteUser(self, user):
        print(str(user.getNeme()))



    def gotoEmployeeForm(self, event):
        self.container.viewUserForm()

    def logout(self, event):
        self.container.viewLogin()

    def back(self, event):
        self.container.viewMenu(self.container.isEmployee)


    def getMainGeometry(self):
        return "470x400"
    def getMainTitle(self):
        return "User List"

