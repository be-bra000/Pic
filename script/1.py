request = int(input("Введите номер кабирнета: "))
dictionary ={
    101: {'key': 1234, 'access': True},
    102: {'key': 1233, 'access': True},
    103: {'key': 1324, 'access': True},
    104: {'key': 4444, 'access': False},
    None: {'key': None, 'access': False}
}
response = dictionary.get(request)
if not response:
    response=dictionary[None]
key = response.get('key')
access = response.get('access')
print(key, access)
