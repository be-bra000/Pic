from typing import List, Tuple

def process_user_data() -> Tuple[List[int], Tuple[int, ...]]:

    input_str = input("Введите числа, разделенные пробелом: ")
    str_list = input_str.split()
    int_list = []
    for item in str_list:
        try:
            int_list.append(int(item))
        except ValueError:
            print(f"Предупреждение: '{item}' пропущено (не является целым числом).")

    result_list = int_list
    result_tuple = tuple(int_list)
    return result_list, result_tuple
result_list, result_tuple = process_user_data()

print("\n--- Результат ---")
print(f"Список: {result_list}")
print(f"Кортеж: {result_tuple}")