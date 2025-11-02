class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        return f"'{self.title}' - {self.author}"


class Ebook(Book):
    def __init__(self, title, author, pages, size):
        super().__init__(title, author, pages)
        self.size = size

    def info(self):
        return f"Ebook: '{self.title}' - {self.size}MB"


ebook1 = Ebook("1984", "Оруэлл", 328, 5)
print(ebook1.info())