from tkinter import *

class EmployeeMenuForm(Frame):

    def __init__(self, master):
        """ Initialize the Frame. """

        super(EmployeeMenuForm, self).__init__(master)
        self.master = master
        # self.controller = controller

        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.book_btn = Button(self, text="Book Manage")
        self.book_btn.grid(sticky=W)
        self.book_btn.bind('<Button-1>', self.bookManage)

        self.emp_btn = Button(self, text="Employee Manage")
        self.emp_btn.grid(sticky=W)
        self.emp_btn.bind('<Button-1>', self.empManage)

        self.borrow_list_btn = Button(self, text="Borrow List")
        self.borrow_list_btn.grid(sticky=W)
        self.borrow_list_btn.bind('<Button-1>', self.borrow)

        self.cancel_btn = Button(self, text="Cancel")
        self.cancel_btn.grid(sticky=W)
        self.cancel_btn.bind('<Button-1>', self.cancel)

    def bookManage(self, event):
        print("book button Clicked")

    def empManage(self, event):
        print("emp button Clicked")

    def borrow(self, event):
        print("borrow button Clicked")

    def cancel(self, event):
        print("Cancel button Clicked")


root = Tk()
root.title("Employee Menu")
root.geometry("200x120")
test = EmployeeMenuForm(root)
root.mainloop()

