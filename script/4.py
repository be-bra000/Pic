lists_of_grades = [
    [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4],
    [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4],
    [5, 4, 3, 3, 3, 4, 3, 5, 5, 3, 3, 3, 3, 4, 4]
]

updated_lists = []

for grades in lists_of_grades:
    updated_grades = grades.copy()

    for i in range(len(updated_grades)):
        if updated_grades[i] == 2:
            updated_grades[i] = 4

    updated_lists.append(updated_grades)

print("\n--- Обновленные списки оценок (2 заменены на 4) ---")
for i, lst in enumerate(updated_lists):
    print(f"Список {i + 1}: {lst}")