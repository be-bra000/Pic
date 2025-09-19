# Создать логин для пользователя на основе его имени и фамилии.
first_name = input("Введите ваше имя: ")
last_name = input("Введите вашу фамилию: ")
login = (first_name[0] + last_name).lower()
print(f"Ваш сгенерированный логин: {login}")

from datetime import date
today = date.today()
print("Дата:", today)