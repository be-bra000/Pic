import time
from functools import wraps


def time_of(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        result_time = end_time - start_time

        print(f"\n--- Время выполнения функции '{func.__name__}': {result_time:.6f} сек ---")
        return result
    return wrapper


@time_of
def fibonacci():
    fib1 = fib2 = 1

    print(fib1, fib2, end=' ')

    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end=' ')
    print()


if __name__ == '__main__':
    fibonacci()