from tkinter import Tk
from loginUI import *
from studentFormUI import *
from userFormUI import *
from studentListUI import *
from userListUI import *
from menuUI import *
from bookListUI import *
from bookUI import *

from library import *
from user import *

class Container(object):

    def __init__(self):

        self.library = Library(name="Demo", brunch_name="Dhaka", address="DU", phone_no="01766539369")
        user1 = User(name="User1", address="Address1", phone_no="Phone", user_name="admin", password="admin")
        user2 = User(name="User2", address="Address2", phone_no="Phone", user_name="admin", password="admin")
        student = Student(name="Stu1", address="Stu add 1", phone_no="Phone", user_name="stu", password="stu")
        self.library.addUser(user1)
        self.library.addUser(user2)
        self.library.addStudent(student)
        self.isEmployee = True
        self.root = Tk()
        self.root.title(self.library.getNeme())

        self.addFrame()


        self.show_frame("LoginFrame")

        self.root.mainloop()

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.create_widgets()
        frame.tkraise()
        self.root.geometry(frame.getMainGeometry())
        self.root.title(frame.getMainTitle())


    def viewLogin(self):
        self.show_frame("LoginFrame")

    def viewMenu(self, isEmp):
        self.isEmployee = isEmp
        self.show_frame("MenuFrame")

    def viewBookList(self):
        self.show_frame("BookListFrame")

    def viewBookFormFrame(self):
        self.show_frame("BookFormFrame")


    def viewStudentListFrame(self):
        self.show_frame("StudentListFrame")

    def viewStudentForm(self):
        self.show_frame("StudentFormFrame")


    def viewUserListFrame(self):
        self.show_frame("UserListFrame")

    def viewUserForm(self):
        self.show_frame("UserFormFrame")

    def viewBorrowList(self):
        self.show_frame("UserFormFrame")

    def viewBorrowForm(self):
        self.show_frame("UserFormFrame")

    def viewBorrowForm(self):
        self.show_frame("UserFormFrame")
    def viewBorrowForm(self):
        self.show_frame("UserFormFrame")



    def addFrame(self):
        self.frames = {}

        for F in (LoginFrame, MenuFrame,BookListFrame,BookFormFrame, StudentFormFrame, UserFormFrame, StudentListFrame,UserListFrame):
            page_name = F.__name__
            frame = F(self.root, self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")


if __name__ == "__main__":
    app = Container()