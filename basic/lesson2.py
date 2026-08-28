# ================== STR(строки) =============

# str(строка) - текстовый тип данных 
# тоесть последовательность символов, литералы(обозначение) является '' или "" 
text = "hello my name's Asan" # При использовании апострофа требуется двойные ковычки 

""" Когда вам 
надо
создать
многострочный текст  используем тройные ковычки
"""
#Или
'''
'''
# Свойства:
"""
1) Неизменяемый тип данных
2) Индексируемый тип данных
3) Упорядоченный тип данных
4) Итерируемый тип данных
"""

name = "Асан"
city = 'Бишкек'

greeting = "Привет, " + name + "! "+ "Добро пожаловать в " + city + "!"

print(greeting)


# Индексация строк - Каждый символ строки имеет индекс(позицию), нумерация начинается с 0
string1 = "Hello world!"

# Первый симол
print(string1[0])
print(string1[6])
#Последний символ
print(string1[-1])

# Срезы строк
# [start:stop:step]
print(string1[0:5])
print(string1[::2])
string2 = "123456789"
print(string2[1::2])
# Перевернуть строку 987654321
print(string2[::-1])

string3 = 'Python'
# string3[0] = "J" - не правильно
new_string = "J" + string3[1:]
print(new_string)

# ==== Методы строк =====
string4 = " WoRld " 
print(string4.lower()) # Нижний регистр
print(string4.upper()) # Верхний регистр
print(string4.strip()) #убирает пробелы с обеих сторон
print(string4.lstrip()) # Убирает пробел только слева
print(string4.rstrip()) # Убирает пробел только справа
print(string4.replace('W', "s")) # Заменяет старое значение на новое
string5 = 'ololooooooolo'
print(string5.replace('o', "s", 3)) # Заменить определенное колличество
text1 = "Hellow DS9, I am your teacher"
print(text1.find("DS9"))
print("DS9" in text1)

text2 = "23"
print(text2.isdigit())

