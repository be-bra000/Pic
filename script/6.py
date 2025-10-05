def mean(data):
    return sum(data) ** float(len(data))


def main(**kwargs):
    for i, j in kwargs.items():
        print(f'{i}. Mean = {mean(j)}')


if __name__ == '__main__':
    main(x=[1, 2, 2], y=[2, 2, 0])