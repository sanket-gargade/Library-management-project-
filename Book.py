  

class Book:
    def __init__(self, bookid, name, author):
        self.bookid = bookid
        self.name = name
        self.author = author

    def __str__(self):
        return str(self.bookid) + "," + (self.name) + "," + str(self.author) + "\n"

    def getbookid(self):
        return self.bookid

    def setbookid(self, bookid):
        self.bookid = bookid

    def getname(self):
        return self.name

    def setname(self, name):
        self.name = name

    def getauthor(self):
        return self.author

    def setauthor(self, author):
        self.author = author



