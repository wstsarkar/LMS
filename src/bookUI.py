from tkinter import *


# from student import Student


class BookFormFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(BookFormFrame, self).__init__(master)
        self.master = master
        self.container = container

        self.grid()

    def create_widgets(self):

        for widget in self.winfo_children():
            widget.destroy()

        """ Create login ui that do nothing. """

        self.title_lbl = Label(self, text="Book Title")
        self.title_lbl.grid(row=0, column=0, sticky=E)

        self.title_entry = Entry(self)
        self.title_entry.grid(row=0, column=1)

        self.author_name_lbl = Label(self, text="Author Name")
        self.author_name_lbl.grid(row=1, column=0, sticky=E)

        self.author_name_entry = Entry(self)
        self.author_name_entry.grid(row=1, column=1)

        self.category_lbl = Label(self, text="Category")
        self.category_lbl.grid(row=2, column=0, sticky=E)

        self.category_entry = Entry(self)
        self.category_entry.grid(row=2, column=1)

        self.version_lbl = Label(self, text="Version")
        self.version_lbl.grid(row=3, column=0, sticky=E)

        self.verson_entry = Entry(self)
        self.verson_entry.grid(row=3, column=1)

        self.description_lbl = Label(self, text="Description")
        self.description_lbl.grid(row=4, column=0, sticky=E)

        self.description_entry = Entry(self)
        self.description_entry.grid(row=4, column=1)

        self.stock_lbl = Label(self, text="Stock")
        self.stock_lbl.grid(row=5, column=0, sticky=E)

        self.stock_lbl_entry = Entry(self)
        self.stock_lbl_entry.grid(row=5, column=1)

        self.blank = Label(self, text="")
        self.blank.grid(row=6)

        self.save_btn = Button(self, text="Save")
        self.save_btn.grid(row=7, column=0, sticky=E)
        self.save_btn.bind('<Button-1>', self.save)

        self.cancel_btn = Button(self, text="Cancel")
        self.cancel_btn.grid(row=7, column=1)
        self.cancel_btn.bind('<Button-1>', self.cancel)

        self.message_lbl = Label(self, text="")
        self.message_lbl.grid()

    def save(self, event):
        print("Save button Clicked")

    def cancel(self, event):
        print("Cancel button Clicked")





    def getMainGeometry(self):
        return "200x250"
    def getMainTitle(self):
        return "Add Book"

