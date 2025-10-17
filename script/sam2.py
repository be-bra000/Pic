from typing import Tuple, Any

def remove_first_occurrence(data_tuple: Tuple[Any, ...], value_to_remove: Any) -> Tuple[Any, ...]:
    temp_list = list(data_tuple)
    try:
        index_to_remove = temp_list.index(value_to_remove)
        temp_list.pop(index_to_remove)
    except ValueError:
        pass
    return tuple(temp_list)

test_data_1 = ((1, 2, 3), 1)
test_data_2 = ((1, 2, 3, 1, 2, 3, 4, 5, 2, 3, 4, 2), 3)
test_data_3 = ((2, 4, 6, 6, 4, 2), 9)

print(f"Вход: {test_data_1} -> Ожидается: (2, 3) -> Получено: {remove_first_occurrence(*test_data_1)}")
print(
    f"Вход: {test_data_2} -> Ожидается: (1, 2, 1, 2, 3, 4, 5, 2, 3, 4, 2) -> Получено: {remove_first_occurrence(*test_data_2)}")
print(f"Вход: {test_data_3} -> Ожидается: (2, 4, 6, 6, 4, 2) -> Получено: {remove_first_occurrence(*test_data_3)}")