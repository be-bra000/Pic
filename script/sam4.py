from typing import Tuple, Any

def get_slice_between_id(data_tuple: Tuple[Any, ...], id_element: Any) -> Tuple[Any, ...]:

    try:
        first_index = data_tuple.index(id_element)
    except ValueError:
        return ()
    try:
        second_index = data_tuple.index(id_element, first_index + 1)
        return data_tuple[first_index: second_index + 1]

    except ValueError:
        return data_tuple[first_index:]

test_data_1 = ((1, 2, 3), 8)
test_data_2 = ((1, 8, 3, 4, 8, 9, 2), 8)
test_data_3 = ((1, 2, 8, 5, 1, 2, 9), 8)
test_data_4 = ((1, 8, 3, 4, 8, 9, 8), 8)

print(f"Вход: {test_data_1} -> Ожидается: () -> Получено: {get_slice_between_id(*test_data_1)}")
print(f"Вход: {test_data_2} -> Ожидается: (8, 3, 4, 8) -> Получено: {get_slice_between_id(*test_data_2)}")
print(f"Вход: {test_data_3} -> Ожидается: (8, 5, 1, 2, 9) -> Получено: {get_slice_between_id(*test_data_3)}")
print(f"Вход: {test_data_4} -> Ожидается: (8, 3, 4, 8) -> Получено: {get_slice_between_id(*test_data_4)}")