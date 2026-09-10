# ========== lambda =======
""" 
способ создания функции в одну строку
так же ее называют безымянной функцией
lambda <аргумент>: <выражение>
"""

square = lambda x: x**2
print(square(5))


add = lambda a, b: a+b
print(add(5, 6))


# написать функцию is_even? которая возвращает True если четное 
# иначе False

is_even = lambda num: num % 2 == 0
print(is_even(10))
print(is_even(3))



# =============== map и filter ===============
# map - применяется к каждому элементу итерируемого обьекта
# Синтакксис
# map(<функция>, <итерируемый обьект>)

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr = list(map(lambda x: x **2, list1))
print(sqr)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# если число четное то вывести True если нет то False
result = list(map(lambda num: num % 2 == 0, list2))
print(result)

# filter - оставляет только те элементы итерируемого обьекта 
# для которых функция вернула True
# filter(<функция>, <итерируемый обьект>)

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = list(filter(lambda num: num % 2 == 0, list2))
print(result)


names = ["Асан", "Умар", "Максатбек", "Айсезим", "Раяна"]
result = list(filter(lambda name: len(name)> 4, names))
print(result)

# reduce
from functools import reduce
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(sum(list2))
print(max(list2))
print(min(list2))

# reduce(<функция>, <итерируемый обьект>)
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total = reduce(lambda num1, num2: num1 + num2, list2)
print(total)
total = reduce(lambda num1, num2: num1 * num2, list2)
print(total)


list1 = ['python', 'go', 'javascript', 'c', 'c++']
print(max(list1, key=len))


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(all(num> 0 for num in list2))
print(any(num> 8 for num in list2))

# enumerate
list1 = ['python', 'go', 'javascript', 'c', 'c++']
print(list(enumerate(list1)))

for index, value in enumerate(list1):
    print(index, value)
    


# List comprehension - компактный способ создания нового списка
# из существующего итерируемого обьекта. 
# все пишется в одну строку

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr = [num ** 2 for num in list1]
print(sqr)

result = []
for num in list1:
    result.append(num ** 2)
print(result)

evens = [num for num in list1 if num % 2 == 0]
print(evens)

result = [num if num % 2 == 0 else False  for num in list1 ]
print(result)


# {<key>:<value> <условие1(чтобы применить ко всем)><цикл><условие2(для фильтра)>}
words = ['python', 'go', 'javascript', 'c', 'c++']
result = {word: len(word) for word in words}
print(result)

dict1 = {
    'python': 6,
    'go': 2,
    'javascript': 10,
    'c': 1,
    'c++': 3
}
result = {key: value for key, value in dict1.items() if value > 4}
print(result)


# def a():
#     print("hi")
#     a()
# a()