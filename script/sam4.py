import math
from functools import wraps

def half(func):
    @wraps(func)
    def output_func(*args, **kwargs):
        original_result = func(*args, **kwargs)
        result = original_result / 2
        print(f"[{func.__name__}]: Исходный результат = {original_result}")
        return result
    return output_func
@half
def summ(*args):
    """Складывает все переданные числа."""
    return sum(args)
@half
def mult(*args):
    """Умножает все переданные числа."""
    return math.prod(args)
print("--- Тестирование summ ---")
final_sum = summ(1, 2, 3, 4)
print(f"Результат (половина суммы): {final_sum}\n")

print("--- Тестирование mult ---")
final_mult = mult(1, 2, 3, 4)
print(f"Результат (половина произведения): {final_mult}")