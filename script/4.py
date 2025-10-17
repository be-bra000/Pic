def Pinf(name, age, company = 'eltex'):
    print(f"Имя: {name} Возраст: {age} Компания: {company}")

one = ("Никита", 19)
Pinf(*one)
two = ("Данил", 20, "cisco")
Pinf(*two)