from tkinter import *
from book import *
from container import *


class BorrowBookListFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(BorrowBookListFrame, self).__init__(master)
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
        self.logout_btn.grid(row=0, column=5 + (2 if self.container.isEmployee is True else 0), sticky=E)
        self.logout_btn.bind('<Button-1>', self.logout)

        row = 1

        self.add_book_btn = Button(self, text="Borrow Book")
        self.add_book_btn.grid(row=1, column=0, sticky=W)
        self.add_book_btn.bind('<Button-1>', self.gotoBorrowBook)
        row = 2

        self.selectList = StringVar(self.master)
        self.selectList.trace('w', self.selectList_change)
        self.selectList.set('All List')
        list = ["All List", "Current List"]
        selectListOM = OptionMenu(self, self.selectList, *list)
        selectListOM.config(width=8)
        selectListOM.grid(row=row, column=0, sticky=W)

        self.selectStudent = StringVar(self.master)
        self.selectStudent.trace('w', self.selectStudent_change)
        self.selectStudent.set('Select One')

        if self.container.isEmployee:
            self.selectStudent.set('Select One')
            selectStudentOM = OptionMenu(self, self.selectStudent, *self.container.library.getStudentDropDown())

            selectStudentOM.config(width=10)
            selectStudentOM.grid(row=row, column=1, sticky=W)

    def viewList(self):
        for widget in self.winfo_children():
            grid_info = widget.grid_info()
            if grid_info["row"] > 3:
                widget.destroy()
        row = 3
        Label(self, width=10, text="Title").grid(row=row, column=0, sticky=EW)

        Label(self, width=10, text="author").grid(row=row, column=1, sticky=EW)

        Label(self, width=10, text="Category").grid(row=row, column=2, sticky=EW)

        Label(self, width=10, text="Version").grid(row=row, column=3, sticky=EW)

        Label(self, width=10, text="Description").grid(row=row, column=4, sticky=EW)

        Label(self, width=10, text="Stock").grid(row=row, column=5, sticky=EW)

        if self.container.isEmployee:
            Label(self, text="Action").grid(row=row, column=6, columnspan=2, sticky=EW)

        student_name = self.selectStudent.get()
        student = self.container.library.getStudentByName(student_name)
        if student:
            list = student.allBorrowList if student_name == "All List" else student.currentBorrowList
            if list:
                for book in list:

                    row += 1
                    Label(self, text=book.getTitle()).grid(row=row, column=0, sticky=W)

                    Label(self, text=book.getAuthor()).grid(row=row, column=1, sticky=W)

                    Label(self, text=book.getCategory()).grid(row=row, column=2, sticky=W)

                    Label(self, text=book.getVersion()).grid(row=row, column=3, sticky=W)

                    Label(self, text=book.getDescription()).grid(row=row, column=4, sticky=W)

                    Label(self, text=str(book.getInStock())).grid(row=row, column=5, sticky=W)

                    if self.container.isEmployee:
                        Button(self, text="Return", command=lambda book=book: self.ReturnBook(book)).grid(row=row, column=6, sticky=W)

    def ReturnBook(self, book):
        print(book.getAuthor())

    def selectList_change(self, *args):
        self.viewList()

    def selectStudent_change(self, *args):
        self.viewList()

    def gotoBorrowBook(self, event):
        self.container.viewBorrowForm()

    def logout(self, event):
        self.container.viewLogin()

    def back(self, event):
        self.container.viewMenu(self.container.isEmployee)

    def getMainGeometry(self):
        if self.container.isEmployee:
            return "600x400"
        else:
            return "500x400"

    def getMainTitle(self):
        return "Borrow Book List"
