
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

    def addEmployee(self, employee):
        self.employees.append(employee)

    def removeEmployee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def addCustoemr(self, customer):
        self.customers.append(customer)

    def removeCustomer(self, customer):
        if customer in self.customers:
            self.customers.remove(customer)