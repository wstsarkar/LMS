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
        self.create_widgets()

    def create_widgets(self):
        """ Create login ui that do nothing. """
        row = 1
        Label(self, text="Title").grid(row=0, column=0, sticky=EW)

        Label(self, text="author").grid(row=0, column=1, sticky=EW)
        for book in self.container.library.getAllBook():

            Label(self, text=book.getTitle()).grid(row=row, column=0, sticky=W)

            Label(self, text=book.getAuthor()).grid(row=row, column=1, sticky=W)
            row += 1

    def getMainGeometry(self):
        return "300x400"
    def getMainTitle(self):
        return "Student List"

