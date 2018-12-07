from tkinter import *


class BookFormFrame(Frame):

    def __init__(self, master, controller):
        """ Initialize the Frame. """

        super(BookFormFrame, self).__init__(master)
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


        self.manager_admin_chk_btn = Checkbutton(self, text="Manager Admin")
        self.manager_admin_chk_btn.grid()

        self.save_btn = Button(self, text="Save")
        self.save_btn.grid()
        self.save_btn.bind('<Button-1>', self.save)

        self.cancel_btn = Button(self, text="Cancel")
        self.cancel_btn.grid()
        self.cancel_btn.bind('<Button-1>', self.cancel)

        self.message_lbl = Label(self, text="")
        self.message_lbl.grid()

    def save(self, event):
        self.message_lbl.config(text="Success")

    def cancel(self, event):
        self.controller.viewLogin()

