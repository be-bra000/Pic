# sam4.py - Инкапсуляция
class Book:
    def __init__(self, title, price):
        self.title = title
        self.__price = price

    def get_price(self):
        return f"Цена: {self.__price} руб."

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
            return "Цена изменена"
        return "Ошибка цены"


book3 = Book("Война и мир", 500)
print(book3.get_price())
print(book3.set_price(600))
print(book3.get_price())