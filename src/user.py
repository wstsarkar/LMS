
class User(object):
    no_of_user = 0

    def __init__(self, name, address, phone_no, user_name, password):
        User.no_of_user += 1

        self.name = name
        self.address = address
        self.phone_no = phone_no
        self.user_name = user_name
        self.password = password

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

