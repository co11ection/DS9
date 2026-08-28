# ============ Словарь(dict)==============
# dict - изменяемый, итерируемый, неупорядочеенный(лжеупорядоченный), не индексируемый тип данных
# для хранения в парах {key: value}
# key - может быть только не изменяемые типы данных
# value - без разницы
# литералы - {key: value}

# [1,2,3] -> 48645879
# [1,2,3] -> 56798764

# ["0775757568", '0778645678']

user = {
    "name": "Aktan",
    "age": 19,
    "last_name": 'Asanov'
}

print(user['name'])
print(user['age'])
print(user['last_name'])

dict1 = {
    "a": 1, "b": 2, "c": 4, "a": 5
}
# Если ключи повторяются то сохраняется последнее значение
print(dict1)

# Создание словарей
dict1 = {1: "a"}
dict2 = dict([(1, "a"), (2, 'b')])
print(dict2)
dict3 = dict([("ab"), ("bc")])
print(dict3)

dict5 = {}
print(dict5)
dict5['name'] = "John"
dict5['age'] = 20
print(dict5)

# ====== Методы словарей =======
user = {
    "name": "Aktan",
    "age": 19,
    "last_name": 'Asanov'
}

# print(user['second_name']) KeyError: 'second_name'

# get() - метод, который возвращает значение по ключу, но если ключа нету возвращает None(пустоту) или дефолтное значение которое вы передали

print(user.get('second_name'))
print(user.get('name'))
print(user.get('second_name', "Такого ключа нету!!!"))

# pop() - удаляет по ключу и возвращает значение
dict1 = {"a": 1, "b": 2}
popped = dict1.pop('a')
print(dict1)
print(popped)

# popitem() - удаляет последнюю пару(ключ-значение) и возвращает его
dict1 = {"a": 1, "b": 2}
popped = dict1.popitem()
print(dict1)
print(popped)

# update() - расширяет словарь парами из второго словаря
dict1 = {"a": 1, "b": 2}
dict2 = {'c': 3, "d": 4, 'b': 3}

dict1.update(dict2)
print(dict1)
dict1.update({'e': 5})
print(dict1)

# clear - очищает словарь
dict1.clear()
print(dict1)

dict2 = dict.fromkeys('hi', 'hello')
print(dict2)

dict3 = dict.fromkeys([1,2,3], 'дефолтное значение')
print(dict3)

user = {
    "name": "John",
    'age': 20,
    "last_name": "Snow"
}
# keys() - метод, который возвращает ключи
print(user.keys())

# values() - метод, который возвращает значения
print(user.values())

# items() - метод, который возвращает пары ключ значение в виде tuple
print(user.items())


# ============= Практика =========
user = {
    'name': "Aibek",
    'age': 25
}
# добавить ключ city со значением Bishkek
user["city"] = "Bishkek"
print(user)

car = {
    'brand': "Toyota",
    'model': "Camry",
    'year': 2020,
    'color': 'white'
}
# удалить ключ color со значением white
car.pop('color')
print(car)
