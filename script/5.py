def main(**kwargs):
    for i in kwargs.items():
        print(i[0], i[1])
    print()
    for key in kwargs:
        print(f'{key} = {kwargs[key]}')


my_dict = {
    'x': [3, 2, 1],
    'y': [3, 2, 0],
    'z': [2, 1, 0],
    'q': [3, 1, 0],
    'w': [3, 2, 0]
}
main(**my_dict)