from book import *


class Student(object):
    no_of_student = 0

    def __init__(self, name, address, phone_no, user_name, password):
        Student.no_of_student += 1

        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.user_name = user_name
        self.password = password

        self.currentBorrowList = []
        self.allBorrowList = []
        self.allReturnList = []

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

    def getUserName(self):
        return self.user_name

    def changeUserName(self, user_name):
        self.user_name = user_name

    def getPassword(self):
        return self.password

    def changePassword(self, password):
        self.password = password

    def borrowBook(self, book):
        if book not in self.currentBorrowList:
            self.currentBorrowList.append(book)
            self.allBorrowList.append(book)
            book.borrowedBook()
            return True
        else:
            return False

    def returnBook(self, book):
        if book in self.currentBorrowList:
            self.currentBorrowList.remove(book)
            self.allReturnList.append(book)
            book.returnedBook()
            return True
        else:
            return False


    def getBorrowedCurrentList(self):
        return self.currebtBorrowList

    def getBorrowedHistory(self):
        return self.allReturnList

    def getReturnedList(self):
        return self.allReturnList

