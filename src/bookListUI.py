
from tkinter import *
from book import *
from container import *


class BookListFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(BookListFrame, self).__init__(master)
        self.master = master
        self.container = container


        self.grid()

    def create_widgets(self):

        for widget in self.winfo_children():
            widget.destroy()

        """ Create login ui that do nothing. """
        row = 1
        Label(self, text="Title").grid(row=0, column=0, sticky=EW)

        Label(self, text="author").grid(row=0, column=1, sticky=EW)

        Label(self, text="Category").grid(row=0, column=2, sticky=EW)

        Label(self, text="Version").grid(row=0, column=3, sticky=EW)

        Label(self, text="Description").grid(row=0, column=4, sticky=EW)

        Label(self, text="Stock").grid(row=0, column=5, sticky=EW)

        for book in self.container.library.getAllBook():

            Label(self, text=book.getTitle()).grid(row=row, column=0, sticky=W)

            Label(self, text=book.getAuthor()).grid(row=row, column=1, sticky=W)

            Label(self, text=book.getCategory()).grid(row=row, column=2, sticky=W)

            Label(self, text=book.getVersion()).grid(row=row, column=3, sticky=W)

            Label(self, text=book.getDescription()).grid(row=row, column=4, sticky=W)

            Label(self, text=book.getCount()).grid(row=row, column=5, sticky=W)
            row += 1

    def getMainGeometry(self):
        return "400x400"
    def getMainTitle(self):
        return "Book List"

