import datetime

FNAME = '4.txt'

def new_exp():
    cat = input("\nКатегория: ").strip()
    while True:
        try:
            summa = float(input("Сумма (число): "))
            if summa > 0:
                break
            print("Сумма должна быть > 0.")
        except ValueError:
            print("Неверный ввод.")

    date_str = datetime.date.today().strftime("%Y-%m-%d")
    log_line = f"{date_str}|{cat}|{summa:.2f}\n"

    try:
        with open(FNAME, 'a', encoding='utf-8') as f:
            f.write(log_line)
        print("Записано.")
    except:
        print(f"Ошибка записи в {FNAME}")

def show_data():
    total = 0.0

    try:
        with open(FNAME, 'r', encoding='utf-8') as f:
            lines = f.readlines()

            if not lines:
                print("\nЖурнал пуст.")
                return

            print("\n--- Отчет ---")
            print("Дата        | Категория     | Сумма (руб.)")
            print("------------------------------------------")

            for line in lines:
                try:
                    d, c, a_str = line.strip().split('|')
                    a = float(a_str)
                    total += a
                    print(f"{d:<10} | {c:<13} | {a:>10.2f}")
                except:
                    continue

            print("------------------------------------------")
            print(f"ИТОГО: {'':<28} {total:>10.2f} руб.")

    except FileNotFoundError:
        print(f"\nФайл '{FNAME}' не найден.")


def run_app():
    while True:
        print("\n=== ФИНАНСЫ ===")
        print("1. Добавить расход")
        print("2. Показать отчет")
        print("3. Выход")

        choice = input("Опция (1-3): ").strip()

        if choice == '1':
            new_exp()
        elif choice == '2':
            show_data()
        elif choice == '3':
            print("Выход.")
            break
        else:
            print("Неверная опция.")

if __name__ == "__main__":
    run_app()