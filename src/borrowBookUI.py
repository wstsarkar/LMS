
from tkinter import *
from book import *
from container import *


class BorrowBookFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(BorrowBookFrame, self).__init__(master)
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
        self.logout_btn.grid(row=0, column=5 + (2 if self.container.isEmployee == True else 0), sticky=E)
        self.logout_btn.bind('<Button-1>', self.logout)

        row = 1

        self.selectStudent = StringVar(self.master)
        self.selectStudent.set('Select One')

        selectStudentOM = OptionMenu(self, self.selectStudent, *self.container.library.getStudentDropDown())

        selectStudentOM.grid(row=row, column=0, columnspan=3, sticky=W)

        row = 2

        Label(self, text="Title").grid(row=row, column=0, sticky=EW)

        Label(self, text="author").grid(row=row, column=1, sticky=EW)

        Label(self, text="Category").grid(row=row, column=2, sticky=EW)

        Label(self, text="Version").grid(row=row, column=3, sticky=EW)

        Label(self, text="Description").grid(row=row, column=4, sticky=EW)

        Label(self, text="Stock").grid(row=row, column=5, sticky=EW)

        Label(self, text="Action").grid(row=row, column=6, columnspan=2, sticky=EW)

        for book in self.container.library.getAllBook():

            row += 1
            Label(self, text=book.getTitle()).grid(row=row, column=0, sticky=W)

            Label(self, text=book.getAuthor()).grid(row=row, column=1, sticky=W)

            Label(self, text=book.getCategory()).grid(row=row, column=2, sticky=W)

            Label(self, text=book.getVersion()).grid(row=row, column=3, sticky=W)

            Label(self, text=book.getDescription()).grid(row=row, column=4, sticky=W)

            Label(self, text=str(book.getInStock())).grid(row=row, column=5, sticky=W)

            Button(self, text="Borrow", command=lambda book=book: self.BorrowBook(book)).grid(row=row, column=6, sticky=W)


    def BorrowBook(self, book):

        student_name = self.selectStudent.get()
        if student_name != "Select One":
            self.container.library.getStudentByName(student_name).borrowBook(book)

        print(book.getTitle())

    def gotoBookForm(self, event):
        self.container.viewBookFormFrame()

    def logout(self, event):
        self.container.viewLogin()

    def back(self, event):
        self.container.viewMenu(self.container.isEmployee)

    def getMainGeometry(self):
        if self.container.isEmployee:
            return "450x400"
        else:
            return "420x400"
    def getMainTitle(self):
        return "Book List"

