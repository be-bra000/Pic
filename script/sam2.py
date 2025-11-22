def fib(n):
    a, b = 1, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

with open('fib.txt', 'w', encoding='utf-8') as file:
    for i, num in enumerate(fib(200), 1):
        file.write(f"F({i}) = {num}\n")

print(f"\nВсего записано 200 чисел ФибонФаччи в файл 'fib.txt'")