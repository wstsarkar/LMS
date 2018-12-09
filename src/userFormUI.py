from tkinter import *
from user import User


class UserFormFrame(Frame):

    def __init__(self, master, container):
        """ Initialize the Frame. """

        super(UserFormFrame, self).__init__(master)
        self.master = master
        self.container = container

        self.grid()

    def create_widgets(self):

        for widget in self.winfo_children():
            widget.destroy()

        self.name_lbl = Label(self, text="Name")
        self.name_lbl.grid(row=0, column=0, sticky=E)

        self.name_entry = Entry(self)
        self.name_entry.grid(row=0, column=1)

        self.address_lbl = Label(self, text="Address")
        self.address_lbl.grid(row=1, column=0, sticky=E)

        self.address = Entry(self)
        self.address.grid(row=1, column=1)

        self.phone_no_lbl = Label(self, text="Phone No")
        self.phone_no_lbl.grid(row=2, column=0, sticky=E)

        self.phone_no = Entry(self)
        self.phone_no.grid(row=2, column=1)

        self.user_name_lbl = Label(self, text="User Name")
        self.user_name_lbl.grid(row=3, column=0, sticky=E)

        self.user_name = Entry(self)
        self.user_name.grid(row=3, column=1)

        self.password_lbl = Label(self, text="Password")
        self.password_lbl.grid(row=4, column=0, sticky=E)

        self.password = Entry(self)
        self.password.grid(row=4, column=1)

        self.blank = Label(self, text="")
        self.blank.grid(row=5)

        self.save_btn = Button(self, text="Save")
        self.save_btn.grid(row=6, column=0, sticky=E)
        self.save_btn.bind('<Button-1>', self.save)

        self.cancel_btn = Button(self, text="Cancel")
        self.cancel_btn.grid(row=6, column=1)
        self.cancel_btn.bind('<Button-1>', self.cancel)

        self.message_lbl = Label(self, text="")
        self.message_lbl.grid()


    def save(self, event):
        name = self.name_entry.get()
        address = self.address.get()
        phone_no = self.phone_no.get()
        user_name = self.user_name.get()
        password = self.password.get()
        user = User(name, address, phone_no, user_name, password)
        self.container.library.addUser(user)
        user = None
        self.container.viewMenu(self.container.isEmployee)



    def cancel(self, event):
        self.container.viewMenu(self.container.isEmployee)






    def getMainGeometry(self):
        return "200x250"
    def getMainTitle(self):
        return "Add Employee"