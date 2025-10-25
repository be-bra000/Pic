import string

def get_text_stats(filepath):
    total_lines = 0
    total_words = 0
    total_letters = 0
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                total_lines += 1
                words_list = line.split()
                total_words += len(words_list)
                for char in line:
                    if char in string.ascii_letters:
                        total_letters += 1

    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return

    print(f"{total_letters} letters")
    print(f"{total_words} words")
    print(f"{total_lines} lines")

if __name__ == "__main__":
    get_text_stats('5.txt')