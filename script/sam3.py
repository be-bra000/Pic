def calculate_average(*args):

    if not args:
        return 0

    total_sum = sum(args)
    count = len(args)

    return total_sum / count

if __name__ == "__main__":
    result1 = calculate_average(10, 20, 30)
    print(f"Среднее для (10, 20, 30): {result1}")

    result2 = calculate_average(2, 4, 6, 8, 10, 12)
    print(f"Среднее для (2, 4, 6, 8, 10, 12): {result2}")

    result3 = calculate_average(15)
    print(f"Среднее для (15): {result3}")