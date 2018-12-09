
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
        if self.container.isEmployee:
            self.add_book_btn = Button(self, text="Add Book")
            self.add_book_btn.grid(row=1, column=0, sticky=W)
            self.add_book_btn.bind('<Button-1>', self.gotoBookForm)
            row = 2



        Label(self, text="Title").grid(row=row, column=0, sticky=EW)

        Label(self, text="author").grid(row=row, column=1, sticky=EW)

        Label(self, text="Category").grid(row=row, column=2, sticky=EW)

        Label(self, text="Version").grid(row=row, column=3, sticky=EW)

        Label(self, text="Description").grid(row=row, column=4, sticky=EW)

        Label(self, text="Stock").grid(row=row, column=5, sticky=EW)

        if self.container.isEmployee:
            Label(self, text="Action").grid(row=row, column=6, columnspan=2, sticky=EW)

        for book in self.container.library.getAllBook():

            row += 1
            Label(self, text=book.getTitle()).grid(row=row, column=0, sticky=W)

            Label(self, text=book.getAuthor()).grid(row=row, column=1, sticky=W)

            Label(self, text=book.getCategory()).grid(row=row, column=2, sticky=W)

            Label(self, text=book.getVersion()).grid(row=row, column=3, sticky=W)

            Label(self, text=book.getDescription()).grid(row=row, column=4, sticky=W)

            Label(self, text=book.getCount()).grid(row=row, column=5, sticky=W)

            if self.container.isEmployee:
                Button(self, text="Edit").grid(row=row, column=6, sticky=EW)
                Button(self, text="Delete").grid(row=row, column=7, sticky=EW)


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

