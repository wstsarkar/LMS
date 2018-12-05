from tkinter import Tk
from loginUI import *
from studentFormUI import *
from userFormUI import *

class Container(object):

    def __init__(self):
        self.root = Tk()

        self.frames = {}

        for F in (LoginFrame, StudentFormFrame, UserFormFrame):
            page_name = F.__name__
            frame = F(self.root, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginFrame")

        self.root.mainloop()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()

    def viewStudentForm(self):
        self.show_frame("StudentFormFrame")

    def viewLogin(self):
        self.show_frame("LoginFrame")

    def viewUserForm(self):
        self.show_frame("UserFormFrame")





if __name__ == "__main__":
    app = Container()