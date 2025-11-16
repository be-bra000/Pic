def plus_two():
    try:
        user_input = input("Введите число, которое нужно сложить с 2: ")
        b = int(user_input)
        result = 2 + b
        return result
    except ValueError:
        print("Ошибка: Неподходящий тип данных. Ожидалось число.")
        return None

print("\n--- Тест 1: Успешное выполнение (Ожидаем результат) ---")
test1 = plus_two()
if test1 is not None:
    print(f"Результат сложения: {test1}")

print("\n--- Тест 2: Неудачное выполнение (Ожидаем ошибку 'Неподходящий тип данных...') ---")
test2 = plus_two()
if test2 is not None:
    print(f"Результат сложения: {test2}")

print("\n--- Тест 3: Успешное выполнение с отрицательным числом (Ожидаем результат) ---")
test3 = plus_two()
if test3 is not None:
    print(f"Результат сложения: {test3}")