from tkinter import *
from student import Student
from container import *


class StudentListFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(StudentListFrame, self).__init__(master)
        self.master = master
        self.container = container

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create login ui that do nothing. """
        row = 0
        for user in self.container.library.getAllUser():

            Label(self, text="Name :").grid(row=row, sticky=W)

            Label(self, text=user.getNeme()).grid(row=row, column=1, sticky=W)

            Label(self, text="Address :").grid(row=row + 1, sticky=W)

            Label(self, text=user.getAddress()).grid(row=row + 1, column=1, sticky=W)
            row += 2


