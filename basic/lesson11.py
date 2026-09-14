# ================== Декораторы =============
""" 
Функция высшего порядка - функция которая принимает аргументом другую функцию
создает внутри себя функцию, вызывает функцию и так же возвращает функцию

Декораторы - функция высшего порядка, которая нужна чтобы расширить функцию не меняя ее функционал
это просто функция обертка
"""

def decorator1(func):
    def wrapper(*args, **kwargs):
        from datetime import datetime
        print('start', datetime.now())
        func(*args, **kwargs)
        print('finish', datetime.now())
        
    return wrapper


@decorator1
def bye():
    print('bye bye')


bye()

# ======= Практика ========
"""
Создать декоратор call_counter, 
который считает,
сколько раз была вызвана функция.
"""
def call_counter(func):
    count = 0
    def wrapper(*args, **kwargs):
        nonlocal count
        count+=1
        print(f"Функция вызвана {count} раз")
        return func(*args, **kwargs)
    return wrapper

@call_counter
def bye():
    print('bye bye')
    

bye()
bye()
bye()