def count_phrase_occurrences(filepath):

    search_query = input("Введите искомую букву, фразу или слово: ").strip()

    if not search_query:
        print("Поисковый запрос не может быть пустым.")
        return

    try:
        with open(filepath, 'r', encoding='utf-8') as file_handle:
            file_content = file_handle.read()
        normalized_content = file_content.lower()
        normalized_query = search_query.lower()
        occurrence_count = normalized_content.count(normalized_query)

        print(f"Поисковый запрос: '{search_query}'")
        print(f"Встречается в файле '{filepath}' {occurrence_count} раз(а).")

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

if __name__ == "__main__":
    count_phrase_occurrences('7.txt')