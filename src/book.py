
class Book(object):

    total_book = 0


    def __init__(self, title, author ,category, version ,description, in_stock):
        self.title = title
        self.author = author
        self.category = category
        self.version = version
        self.description = description
        self.in_stock = in_stock
        self.count = in_stock

    def getTitle(self):
        return self.title

    def setTitle(self, title):
        self.title = title

    def getAuthor(self):
        return self.author

    def setAuthor(self, author):
        self.author = author

    def getCategory(self):
        return self.category

    def setCategory(self, category):
        self.category = category

    def getVersion(self):
        return self.version

    def setVersion(self, version):
        self.version = version

    def getDescription(self):
        return self.description

    def setDescription(self, description):
        self.description = description

    def setCount(self,count):
        self.count = count

    def getCount(self):
        return  self.count

    def borrowedBook(self):
        if self.in_stock > 0:
            self.in_stock -= 1
            return True
        else:
            return False

    def returnedBook(self):
        self.in_stock += 1


    def __str__(self):
        return "Title:"+self.title+"\nAuthor:"+self.author+"\nCategory:"+self.category+"\nVersion:"+self.version+"\nDescription:"+self.description

