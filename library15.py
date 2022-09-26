
'''
class student():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def msg(self):
        return self.name + " age is " + str(self.age) + "years old"

o = student("ram", 25)
print(o.name)
print(o.age)
print(o.msg)
'''

class library():
    def __init__(self,books):
        self.books = books

    def listbook(self):
        print("Available books")
        for book in books:
            print(book)

    def borrowbook(self,borrowbook):
        if borrowbook in self.books:
            print("you can take")
            self.books.remove(borrowbook)
        else:
            print("book not available")

    def receivebook(self,receivebook):
        print("you have return the book")
        self.books.append(receivebook)

books = ['C','C++','Java']
o = library(books)

msg = """
    1.List of books
    2.Borrow Books
    3. Receive books
"""
while True:
    print(msg)
    ch = int(input("enter:"))
    if ch == 1:
        o.listbook()
    elif ch == 2:
        print(books)
        book = input("enter book: ")
        o.borrowbook(book)
    elif ch == 3:
        book = input("enter book: ")
        o.receivebook(book)
    else:
        print("tq")
quit()
