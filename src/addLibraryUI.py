from tkinter import *

class LibraryFormFrame(Frame):

    def __init__(self, master):
        """ Initialize the Frame. """

        super(LibraryFormFrame, self).__init__(master)
        self.master = master
        #self.controller = controller

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create login ui that do nothing. """

        self.lib_name_lbl = Label(self, text="Library Name")
        self.lib_name_lbl.grid(row=0, column=0, sticky=E)

        self.lib_name_entry = Entry(self)
        self.lib_name_entry.grid(row=0, column=1)

        self.branch_name_lbl = Label(self, text="Branch Name")
        self.branch_name_lbl.grid(row=1, column=0, sticky=E)

        self.branch_name_entry = Entry(self)
        self.branch_name_entry.grid(row=1, column=1)

        self.address_lbl = Label(self, text="Address")
        self.address_lbl.grid(row=2, column=0, sticky=E)

        self.address_entry = Entry(self)
        self.address_entry.grid(row=2, column=1)

        self.phone_no_lbl = Label(self, text="Phone No")
        self.phone_no_lbl.grid(row=3, column=0, sticky=E)

        self.phone_no = Entry(self)
        self.phone_no.grid(row=3, column=1)

        self.blank = Label(self, text="")
        self.blank.grid(row=4)

        self.save_btn = Button(self, text="Save")
        self.save_btn.grid(row=5, column=0, sticky=E)
        self.save_btn.bind('<Button-1>', self.save)


        self.cancel_btn = Button(self, text="Cancel")
        self.cancel_btn.grid(row=5, column=1)
        self.cancel_btn.bind('<Button-1>', self.cancel)

        self.message_lbl = Label(self, text="")
        self.message_lbl.grid()

    def save(self, event):
        print("Save button Clicked")

    def cancel(self, event):

        print("Cancel button Clicked")

root = Tk()
root.title("Library Form")
root.geometry("200x150")
test = LibraryFormFrame(root)
root.mainloop()

