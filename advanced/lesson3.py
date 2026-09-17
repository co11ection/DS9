# ============== Файлы и работа с ними ==========
# Файл это структура данных которые сохраняются на диске компьютера
# адрес - это пусть к нашему файлу
# относительный путь - DS9(.)/advanced/lesson3.py
# абсолютный путь - /Users/macbook/Desktop/DS9/advanced/lesson3.py

# ======== функция open, режимы, чтение файла========
# Основные режимы
""" 
'r' - чтение
'w' - запись(перезаписывает данные), так же создает файл
'a' - добавить
'x' - создает файл(если файл уже создан то выдает ошибку)
"""
# Прочтение
try:
    file = open(file="advanced/test.txt", mode='r', encoding='utf-8')
    print(file.read()) # Полное прочтение
    file.seek(0)
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.close()
except FileNotFoundError:
    print("файл не найден")

# Запись (перезапись) режим w
try:
    file = open(file="test.txt", mode='w', encoding='utf-8')
    file.write("Привет мир!\n")
    file.write("Привет мир!2\n")
    file.close()
except FileNotFoundError:
    print("файл не найден")

# Добавление и режим 'a' отличие от 'w'
try:
    file = open(file="test.txt", mode='a', encoding='utf-8')
    file.write("Привет мир!3\n")
    file.write("Привет мир!4\n")
    file.close()
except FileNotFoundError:
    print("файл не найден")


# Напишите код который будет создавать файл color.txt и записывать в него три ваших любимых цвета и каждый цвет должен быть на новой строке
try:
    file = open(file="color.txt", mode='w', encoding='utf-8')
    file.write("Черный\n")
    file.write("Белый\n")
    file.write("Синий\n")
    file.close()
except FileNotFoundError:
    print("файл не найден")
    
# Чтение с помощью цикла
try:
    file = open(file="color.txt", mode='r', encoding='utf-8')
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("файл не найден")
    
# Контекстный менеджер
with open(file='color.txt', mode='r+', encoding='utf-8') as file:
    lines = file.read()
    file.write('фиолетовый')
    print(lines)


# with open(file='color.txt', mode='w+', encoding='utf-8') as file:
#     file.write('бордовый')
#     file.seek(0)
#     print(file.read())


# 1) Написать функцию add_notes(), которая дозаписывает строку text в файл notes.txt
# 2) Написать функцию read_notes() которая возвращает список всех заметом
# 3) Написать функцию show_notes() которая вызывает функцию read_notes() и показывает все заметки в виде 
# 1. первая заметка 
# 2. вторая заметка
# Если заметок нету то должно показать "Заметок пока что нет"

def add_notes():
    text = input("Наишите заметку: ")
    with open(file="notes.txt", mode='a', encoding='utf-8') as file:
        file.write(text + '\n')
    
    return 'Заметка сохранена'

# print(add_notes())

def read_notes():
    with open(file="notes.txt", mode='r', encoding='utf-8') as file:
        return file.readlines()
    
print(read_notes())