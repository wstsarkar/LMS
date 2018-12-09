from book import *
from user import *
from student import *

class Library(object):


    def __init__(self, name, brunch_name, address, phone_no):

        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.brunch_name = brunch_name

        self.books = []
        self.users = []
        self.students = []


    def getNeme(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAddress(self):
        return self.address

    def setAddress(self, address):
        self.address = address

    def getPhoneNo(self):
        return self.phone_no

    def setPhoneNo(self, phone_no):
        self.address = phone_no

    def getBrunchName(self):
        return self.brunch_name

    def setBrunchName(self, brunch_name):
        self.brunch_name = brunch_name

    def addBook(self, book):
        self.books.append(book)

    def deleteBook(self, book):
        if book in self.books:
            self.books.remove(book)

    def addUser(self, user):
        self.users.append(user)

    def deleteUser(self, user):
        if user in self.users:
            self.users.remove(user)

    def addStudent(self, student):
        self.students.append(student)

    def deleteStudent(self, student):
        if student in self.students:
            self.student.remove(student)

    def getAllUser(self):
                return self.users
    def getAllBook(self):
        return self.books

    def getAllStudent(self):
        return self.students


    def getStudentDropDown(self):
        temp=[]
        temp.append("Select One")
        for student in self.students:
            temp.append(student.getNeme())
        return temp
