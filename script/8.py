from random import randint

def list_maker():
    value = randint(1, 100)
    count = randint(3, 10)
    a = [value] * count
    return a


if __name__ == '__main__':
    result = []
    num_lists = randint(1, 5)

    for i in range(num_lists):
        result.append(list_maker())

    print(f"Сгенерированный n-мерный список из {len(result)} списков: {result}")