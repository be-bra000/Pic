def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

# Вывод чисел Фибоначчи от 200
print("Числа Фибоначчи от 200-го:")
fibonacci_sequence = fib(200)

# Получаем все числа, но нам нужно только 200-е
result = None
for i, num in enumerate(fibonacci_sequence, 1):
    if i == 200:
        result = num
        break

print(f"200-е число Фибоначчи: {result}")