import os


def check_and_read_file(filename):
    try:
        if not os.path.exists(filename):
            print(f"Ошибка: Файл '{filename}' не найден.")
            return

        if os.path.getsize(filename) == 0:
            raise ValueError("\n--- файл пустой ----")
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            print(f"\n--- Файл '{filename}' не пустой. Содержимое: ---")
            print(content.strip())

    except ValueError as e:
        print(f"\nОшибка при обработке файла '{filename}': {e}")
        print("В консоль выведено: 'файл пустой'")

    except Exception as e:
        print(f"\nПроизошла непредвиденная ошибка с файлом '{filename}': {e}")

check_and_read_file("1.txt")
check_and_read_file("2.txt")