usrNum = int(input("введите свое число: "))
answer = "четное" if usrNum % 2 == 0  else "нечетное"
print(f"число {usrNum} - {answer}")

from datetime import date
today = date.today()
print("Дата:", today)