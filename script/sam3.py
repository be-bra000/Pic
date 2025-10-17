from collections import Counter
from typing import Dict

def get_top_3_counts(digit_string: str) -> Dict[int, int]:
    counts = Counter(int(d) for d in digit_string if d.isdigit())
    top_3 = counts.most_common(3)
    sorted_top_3 = sorted(top_3, key=lambda item: item[0])
    result_dict = dict(sorted_top_3)

    return result_dict

sample_string = "888877766554433221999999"
print(f"Исходная строка: {sample_string}")
result = get_top_3_counts(sample_string)
print("Топ-3 самых частых чисел:")
print(result)