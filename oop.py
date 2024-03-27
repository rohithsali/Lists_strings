class Book:
    def __init__(self, title):
        self.title = title



if __name__ == '__main__':
    Book1 = Book("war and peace")
    Book2 = Book("Harry Potter")
    print(Book1)
    print(Book2.title)
