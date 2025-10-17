def count_vowels(text: str) -> dict:
    vowels = "аеиоуыэюя"
    counts = {}
    lower_text = text.lower()

    for char in lower_text:
        if char in vowels:
            counts[char] = counts.get(char, 0) + 1
    return counts
print("Тест 1:", count_vowels("Привет, Мир!"))
print("Тест 2:", count_vowels("Яблоко"))