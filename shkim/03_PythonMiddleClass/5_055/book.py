class Book:
    def __init__(self, n, p, i):
        self.name = n
        self.price = p
        self.isbn = i


class BookRepository:
    def __init__(self):
        self.books = {}

    def registBook(self, b):
        self.books[b.isbn] = [b.name, b.price]

    def removeBook(self, isbn):
        del self.books[isbn]

    def printBookInfo(self, isbn):
        print('name: {}'.format(self.books[isbn][0]))
        print('price: {}'.format(self.books[isbn][1]))
        print('isbn: {}'.format(isbn))

    def printBooksInfo(self):
        for isbn in self.books.keys():
            self.printBookInfo(isbn)



