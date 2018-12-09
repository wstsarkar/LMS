from tkinter import *
from loginUI import *
from studentFormUI import *
from userFormUI import *
from studentListUI import *

class MenuFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(MenuFrame, self).__init__(master)
        self.master = master
        self.container = container
        self.grid()

        # self.create_user_widgets()

    def create_widgets(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.logout_btn = Button(self, text="Logout")
        self.logout_btn.grid(row=0, column=0, sticky=E)
        self.logout_btn.bind('<Button-1>', self.logout)

        if self.container.isEmployee:
            self.create_user_widgets()
        else:
            self.create_student_widgets()

    def create_user_widgets(self):

        self.book_list_btn = Button(self, text="Book List")
        self.book_list_btn.grid(sticky=E+W)
        self.book_list_btn.bind('<Button-1>', self.gotoBookList)

        self.book_form_btn = Button(self, text="Add Book")
        self.book_form_btn.grid(sticky=E+W)
        self.book_form_btn.bind('<Button-1>', self.gotoBookForm)

        self.student_list_btn = Button(self, text="Student List")
        self.student_list_btn.grid(sticky=E+W)
        self.student_list_btn.bind('<Button-1>', self.gotoStudentList)

        self.student_form_btn = Button(self, text="Add Student")
        self.student_form_btn.grid(sticky=E+W)
        self.student_form_btn.bind('<Button-1>', self.gotoStudentForm)

        self.emp_list_btn = Button(self, text="Employee List")
        self.emp_list_btn.grid(sticky=E+W)
        self.emp_list_btn.bind('<Button-1>', self.gotoEmpList)

        self.emp_form_btn = Button(self, text="Add Employee")
        self.emp_form_btn.grid(sticky=E+W)
        self.emp_form_btn.bind('<Button-1>', self.gotoEmpForm)

        self.borrow_list_btn = Button(self, text="Book Borrow List")
        self.borrow_list_btn.grid(sticky=E+W)
        self.borrow_list_btn.bind('<Button-1>', self.gotoBorrowList)

        self.borrow_form_btn = Button(self, text="Book Borrow")
        self.borrow_form_btn.grid(sticky=E+W)
        self.borrow_form_btn.bind('<Button-1>', self.gotoBorrowForm)

        self.return_list_btn = Button(self, text="Book Return List")
        self.return_list_btn.grid(sticky=E+W)
        self.return_list_btn.bind('<Button-1>', self.gotoReturnList)

        self.return_form_btn = Button(self, text="Book Return")
        self.return_form_btn.grid(sticky=E+W)
        self.return_form_btn.bind('<Button-1>', self.gotoReturnForm)


    def create_student_widgets(self):

        self.book_list_btn = Button(self, text="Book List")
        self.book_list_btn.grid(sticky=E+W)
        self.book_list_btn.bind('<Button-1>', self.gotoBookList)

        self.borrow_list_btn = Button(self, text="Borrow List")
        self.borrow_list_btn.grid(sticky=E+W)
        self.borrow_list_btn.bind('<Button-1>', self.gotoBorrowList)

        self.borrow_form_btn = Button(self, text="Borrow")
        self.borrow_form_btn.grid(sticky=E+W)
        self.borrow_form_btn.bind('<Button-1>', self.gotoBorrowForm)


    def logout(self, event):
        self.container.viewLogin()





    def gotoBookList(self, event):
        self.container.viewBookList()

    def gotoBookForm(self, event):
        self.container.viewBookFormFrame()

    def gotoStudentList(self, event):
        self.container.viewStudentListFrame()

    def gotoStudentForm(self, event):
        self.container.viewStudentForm()

    def gotoEmpList(self, event):
        self.container.viewUserListFrame()

    def gotoEmpForm(self, event):
        self.container.viewUserForm()

    def gotoBorrowList(self, event):
        self.container.viewBorrowList()

    def gotoBorrowForm(self, event):
        self.container.viewBorrowForm()

    def gotoReturnList(self, event):
        self.container.viewReturnList()

    def gotoReturnForm(self, event):
        self.container.viewReturnForm()










    def getMainGeometry(self):
        return "200x350"
    def getMainTitle(self):
        return "Menu"
