from tkinter import *
#from student import Student


class StudentFormFrame(Frame):

    def __init__(self, master):
        """ Initialize the Frame. """

        super(StudentFormFrame, self).__init__(master)
        self.master = master
        #self.controller = controller

        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Create login ui that do nothing. """

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
        print("Save button Clicked")

        """    
        name = self.name_entry.get()
        address = self.address.get()
        phone_no = self.phone_no.get()
        user_name = self.user_name.get()
        password = self.password.get()
        student = Student(name, address, phone_no, user_name, password)
        self.controller.library.addStudent(student)
        student = None
        """



    def cancel(self, event):

        print("Cancel button Clicked")
        """
        self.name_entry.config(text="")
        self.address.config(text="")
        self.phone_no.config(text="")
        self.user_name.config(text="")
        self.password.config(text="")
        """

root = Tk()
root.title("Student Form")
root.geometry("200x180")
test = StudentFormFrame(root)
root.mainloop()

