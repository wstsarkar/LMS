from tkinter import *
from user import *
from container import *


class UserListFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(UserListFrame, self).__init__(master)
        self.master = master
        self.container = container
        self.container.root.title("List")

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create login ui that do nothing. """
        row = 1
        Label(self, text="Name").grid(row=0, column=0, sticky=EW)

        Label(self, text="Address").grid(row=0, column=1, sticky=EW)
        for user in self.container.library.getAllUser():

            Label(self, text=user.getNeme()).grid(row=row, column=0, sticky=W)

            Label(self, text=user.getAddress()).grid(row=row, column=1, sticky=W)

            Button(self, text="Edit", command=lambda: self.deleteUser(user)).grid(row=row, column=1, sticky=W)

            Button(self, text="Delete", command=lambda: self.deleteUser(user)).grid(row=row, column=1, sticky=W)
            row += 1

    def deleteUser(self, user):
        print(str(user.getNeme()))



    def getMainGeometry(self):
        return "300x400"
    def getMainTitle(self):
        return "Student List"

