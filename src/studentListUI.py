from tkinter import *
from student import Student
from container import *


class StudentListFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(StudentListFrame, self).__init__(master)
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

        Label(self, text="Phone No").grid(row=0, column=2, sticky=EW)



        for student in self.container.library.getAllStudent():

            Label(self, text=student.getNeme()).grid(row=row, column=0, sticky=W)

            Label(self, text=student.getAddress()).grid(row=row, column=1, sticky=W)

            Label(self, text=student.getPhoneNo()).grid(row=row, column=2, sticky=W)


            row += 1
    def getMainGeometry(self):
        return "300x400"
    def getMainTitle(self):
        return "Student List"

