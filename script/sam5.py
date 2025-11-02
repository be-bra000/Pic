# sam5.py - Полиморфизм
class Book:
    def description(self):
        return "Это книга"

class Novel(Book):
    def description(self):
        return "Это роман"

class Poetry(Book):
    def description(self):
        return "Это сборник стихов"

books = [Book(), Novel(), Poetry()]
for book in books:
    print(book.description())