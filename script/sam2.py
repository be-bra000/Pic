class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_read = False

    def read(self):
        self.is_read = True
        return f"Прочитали: '{self.title}'"

    def info(self):
        status = "прочитана" if self.is_read else "не прочитана"
        return f"'{self.title}' - {self.author}, {self.pages} стр. ({status})"


book2 = Book("Мастер и Маргарита", "Булгаков", 480)
print("\n2) Атрибуты и методы:")
print(book2.info())
print(book2.read())
print(book2.info())