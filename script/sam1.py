class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_info(self):
        return f"Книга: '{self.title}', автор: {self.author}"

book1 = Book("Преступление и наказание", "Ф.М. Достоевский")
print("1) Создание класса и объекта:")
print(book1.display_info())
print()