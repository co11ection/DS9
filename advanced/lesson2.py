# ================ try except===============
# Обработка исключений
# Ошибка - когда программа не может работать дальше 

# ======== Виды ошибок(со стороны программиста)====
#1) Синтаксическая ошибка - код написан не правильно
# if 5>3 # ожидается :
#     print("Hello")
#     SyntaxError: expected ':'
# def a():
# print("hi")
# IndentationError: expected an indented block after function definition on line 10

# 2)Ошибка выполнения(runtime error)
# Код прописан правильно но возникает проблема самого выполнения
# Это когда долго ждем ответ от сервера, деление на нольт под копотов вызывает RuntimeError
# print(10/0) ZeroDivisionError: division by zero

#3) Логическая ошибка
# Программа работает но выдает неверный результат
# вывести результат если num меньше 20
num = 20
if num<=20:
    print("hi")
# Ожидалось проверка на просто меньше, но было прописано проверка на меньше или равно и поэтому логически решение не правильное

# ====== Исключения ===========
# Вид ошибок которые можно обработать
# ValueError - несоответсвие типов данных
# age = int("hi")

# num = int(input("Введите число: "))

# ZeroDivisionError - при деление на ноль
# print(10/0)

# num1 = int(input("Введите число: "))
# num2 = int(input("Введите число: "))
# print(num1/num2)
# print("end")

# NameError - Когда такого названия(переменной) в файле не ссуществует или обьявленно после использования
# print(name)
# name = 'tima'

# IndexError - Индекса такого не существует
numbers = [1, 2, 3]
# print(numbers[10])


# KeyError - обращение к несуществующему ключу в словаре
student = {
    "name": "Asan",
    "age": 20
}
# print(student['email'])
print(student.get('email'))

# Практика
# print(age) -NameError
# print(23/0) - ZeroDivisionError
# print(int('hello')) - ValueError

# ============ Обработка исключений =====
# Кострукция try/except
# try:
#     <выполняемая программа>
# except <исключение которо мы ожидаем>:
#     <выполняемая программа>

# Если ошибки нету выполняется программа которая находится в теле try
# Если есть ошибка то выполняется то что внутри except
# try:
#     num1 = int(input("Введите число: "))
#     num2 = int(input("Введите число: "))
#     print(num1/num2)
# except ValueError as error:
#     print(f"Ввведите число а не другой тип данных {error}")
# except ZeroDivisionError as error:
#     print(f"Нельзя делить на ноль {error}")
# print("end")


# Запросить у пользователя возраст и обработать ошибку неправильного ввода
# try:
#     age = int(input("Введите возраст: "))
#     print(age)
# except ValueError:
#     print("Нужно ввести число")
    

# else и finally
# блок else - работает только тогда когда ошибки нету

# try:
#     age = int(input("Введите возраст: "))
#     print(age)
# except ValueError:
#     print("Нужно ввести число")
# else:
#     print("else отработал корректно")

# finally- этот блок работает вне зависимоти от ситуации
# try:
#     age = int(input("Введите возраст: "))
#     print(age)
# except ValueError:
#     print("Нужно ввести число")
# else:
#     print("else отработал корректно")
# finally:
#     print("Конец блока")



# ===== генерация исключений (raise)======
# age = int(input("Введите возраст: "))
# if age < 0:
#     raise ValueError("Возраст не может быть меньше 0")

# Получить от пользователя пароль у которого длина должна быть не меньше 6 символов
password = input("Введите пароль: ")
if not password.isalnum():
    raise ValueError("Введите буквы или числа или символы")
if len(password) < 6:
    raise ValueError("Пароль слишком короткий")
