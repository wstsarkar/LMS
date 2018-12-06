from tkinter import *
from student import Student


class StudentFormFrame(Frame):

    def __init__(self, master, controller):
        """ Initialize the Frame. """

        super(StudentFormFrame, self).__init__(master)
        self.master = master
        self.controller = controller

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create login ui that do nothing. """

        self.name_lbl = Label(self, text="Name")
        self.name_lbl.grid()

        self.name_entry = Entry(self)
        self.name_entry.grid()

        self.address_lbl = Label(self, text="Address")
        self.address_lbl.grid()

        self.address = Entry(self)
        self.address.grid()

        self.phone_no_lbl = Label(self, text="Phone No")
        self.phone_no_lbl.grid()

        self.phone_no = Entry(self)
        self.phone_no.grid()

        self.user_name_lbl = Label(self, text="User Name")
        self.user_name_lbl.grid()

        self.user_name = Entry(self)
        self.user_name.grid()

        self.user_name_lbl = Label(self, text="User Name")
        self.user_name_lbl.grid()

        self.user_name = Entry(self)
        self.user_name.grid()

        self.password_lbl = Label(self, text="Password")
        self.password_lbl.grid()

        self.password = Entry(self)
        self.password.grid()

        self.save_btn = Button(self, text="Save")
        self.save_btn.grid()
        self.save_btn.bind('<Button-1>', self.save)

        self.cancel_btn = Button(self, text="Cancel")
        self.cancel_btn.grid()
        self.cancel_btn.bind('<Button-1>', self.cancel)

        self.message_lbl = Label(self, text="")
        self.message_lbl.grid()

    def save(self, event):
        name = self.name_entry.get()
        address = self.address.get()
        phone_no = self.phone_no.get()
        user_name = self.user_name.get()
        password = self.password.get()
        student = Student(name, address, phone_no, user_name, password)
        self.controller.library.addStudent(student)
        student = None


    def cancel(self, event):
        self.name_entry.config(text="")
        self.address.config(text="")
        self.phone_no.config(text="")
        self.user_name.config(text="")
        self.password.config(text="")

