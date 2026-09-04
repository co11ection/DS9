#v================= Функция =================
""" 
Функция - именованный блок кода, 
который можно вызывать сколько угодно раз и где вы хотите
и позволяет соблюдать правила DRY (don't repeat yourself)


"""

# Синтаксис
# def <название функции>(параметры):
#     <тело функции>
#     return <значение которое возвращается>    
# ЕСЛИ ВЫ НЕ ПРОПИШИТЕ return то в таком случае вы получите None


def greet():
    print("Привет!")

greet()

# def square(number, a):
#     return number ** 2

# num = int(input("Введите число: "))
# print(square(num, 4))    
# print(square(125))    
# print(square(5))    


# Параметры - это переменные перечисленные при создании функции
""" 
1)Обязательные
2)Необязательные
    2.1) Дефолтные
    2.2) *args
    2.3) **kwargs
"""
# Аргументы - значения которые передаются при вызове функции
""" 
именованные - нельзя передавать одинаковые параметры при работе с именованными аргументами
позиционные

ПРАВИЛО: когда передаются аргументы при вызове функции нужно для начала передать позиционные аргументы и только потом именованные
"""
# Обязательные параметры
def square(number):
    return number ** 2

# print(square())   TypeError: square() missing 1 required positional argument: 'number'
# Если не передать аргумент для обязательного  параметра то вернется ошибка
print(square(4)) # позиционный
print(square(number=5)) # Именованный

 
# Необезательное
# дефолтные парметры
def greet(name, greeting="Привет"):
    print(f"{greeting}!  {name}")

greet(name="Умар")
greet(name="Умар", greeting='Wellcome')

# *args - попадают лишние позиционные аргументыб и записывает в виде tuple
def print_numbers(a, b, c, *args):
    print("a", a)
    print("b", b)
    print("c", c)
    print("args", args)

print(print_numbers(1,2,3,4,5,6,7,8,9,10,11))

# **kwargs - записывается все лишние именованные аргументы и храняться в виде словари(dict)

def print_numbers(a, b, c, **kwargs):
    print("a", a)
    print("b", b)
    print("c", c)
    print("kwargs", kwargs)
    
print(print_numbers(a=1, b=2, c=3, d=4, e=5, f=8))


def check_age(age):
    if age > 18:
        return "Проходит"
    else:
        return "Не проходит по возрасту"
    
print(check_age(16))

# is_leap_year() - которая возвращает True если год високосный и False если нет (делится без остатка на 4, 100, 400)

def is_leap_year(year):
    if year % 4 != 0:
        return False
    if year % 100 == 0 and year % 400 !=0:
        return False
    return True

print(is_leap_year(2100))
print(is_leap_year(24))
print(is_leap_year(2024))