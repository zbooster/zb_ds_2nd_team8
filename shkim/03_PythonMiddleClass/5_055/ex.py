import book as bk

books = bk.BookRepository()

bName = '데이터 사이언티스트'
bPrice = 15000
bIsbn = '979-11-6005-062-2'

book = bk.Book(bName, bPrice, bIsbn)
books.registBook(book)

books.printBooksInfo()

books.removeBook('979-11-6005-062-2')

books.printBooksInfo()