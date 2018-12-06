from tkinter import Tk
from loginUI import *
from studentFormUI import *
from userFormUI import *
from studentListUI import *

from library import *
from user import *

class Container(object):

    def __init__(self):

        self.library = Library(name="Demo", brunch_name="Dhaka", address="DU", phone_no="01766539369")
        user1 = User(name="User1", address="Address1", phone_no="Phone", user_name="admin", password= "admin")
        user2 = User(name="User2", address="Address2", phone_no="Phone", user_name="admin", password= "admin")
        self.library.addUser(user1)
        self.library.addUser(user2)
        user = None
        self.root = Tk()
        self.root.title(self.library.getNeme())

        self.frames = {}

        for F in (LoginFrame, StudentFormFrame, UserFormFrame,StudentListFrame):
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

    def viewStudentListFrame(self):
        self.show_frame("StudentListFrame")





if __name__ == "__main__":
    app = Container()