import re
from collections import Counter
import string

def analyze_article(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print(f"Ошибка: Файл '{filepath}' не найден.")
        return

    clean_text = re.sub(f'[{re.escape(string.punctuation)}]', ' ', raw_text)
    words = [word for word in clean_text.lower().split() if word and not word.isdigit()]
    word_counts = Counter(words)
    total_word_count = len(words)

    if not word_counts:
        print("В тексте нет слов для анализа.")
        return
    most_frequent_pair = word_counts.most_common(1)[0]

    print(f"Общее количество слов в статье: {total_word_count}")
    print(f"Самое часто встречающееся слово: '{most_frequent_pair[0]}'")
    print(f"Встречается {most_frequent_pair[1]} раз.")

if __name__ == "__main__":
    analyze_article('3.txt')