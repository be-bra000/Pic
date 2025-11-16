class NotIntError(TypeError):

    def __init__(self, arg):
        super().__init__(
            f"Ошибка: Ожидалось целое число (int), "
            f"получен тип '{type(arg).__name__}' (значение: {arg})."
        )

def summ(*args):
    for num in args:
        if not isinstance(num, int):
            raise NotIntError(num)
    return sum(args)
print("--- Тест 1 (Успешно) ---")
try:
    print(f"Сумма: {summ(1, 2, 3, 4)}")
except NotIntError as e:
    print(e)

print("\n--- Тест 2 (Ошибка) ---")
try:
    print(f"Сумма: {summ(2, 4, 4, 'a', 'f')}")
except NotIntError as e:
    print(e)