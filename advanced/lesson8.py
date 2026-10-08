# =============== Итераторы\Генераторы ======================

#----------- Итераторы----------------
#итерируемый обьект - все обьекты, по которым мы можем пройтись циклом является итерируемым

# Итератор - обьект который "ПОМНИТ" на каком месте остановился, и умеет выдавать элемент по одному для этого он использует метод __next__(), у итератора есть __iter__() который возвращает сам себя, тоесть показывая где он находится

list1 = [1, 2, 3, 4, 5]
iter1 = iter(list1)
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))
print(next(iter1))


list1 = [1, 2, 3, 4, 5]

# for i in list1:
#     list1.append(i)
#     print(i)


# Создать список из 4 фруктов, получить через итератор каждый следующий фрукт
# Если вызвать next в 5 раз надо обработать его
fruits = ['яблоко', "банан", "груша", "киви"]
it = iter(fruits)
try:
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
    print(next(it))
except StopIteration:
    print("Элемент закончился")
    


# Как выглядит for под копотом
# fruits = ['яблоко', "банан", "груша", "киви"]
# it = iter(fruits)
# def iterator(iteration_object):
#     while True:
#         try:
#             value =  next(it)
#         except StopIteration:
#             break
#         return value

# print(iterator(it))
# print(iterator(it))
# print(iterator(it))
    

# for i in fruits:
#     print(i)



# class CountNumberDown:
#     def __init__(self, start):
#         self.current = start
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.current < 0:
#             raise StopIteration
#         value = self.current
#         self.current -= 1
#         return value
    
# for num in CountNumberDown(4):
#     print(num)
    
#4
#3
#2
#1
#0


# Создать класс EvenNumbers(start, end) и возвращает только четные числа
class EvenNumbers:
    def __init__(self, start, end):
        self.end = end
        self.current = start if start % 2 == 0 else start + 1
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        
        value = self.current
        self.current += 2
        return value

list1 = list(EvenNumbers(0, 10))
print(list1)


# -------------- Генераторы -------------
# Генератор - это более простой способ итератора в котором в теле функции всмето return используется yield

def count_number_down(start):
    current = start
    while current > 0:
        yield current
        current -=1
        
for num in count_number_down(5):
    print(num)


generor = count_number_down(10)
print(next(generor))
print(next(generor))
print(next(generor))
print(next(generor))



import sys

# list_number = [x for x in range(1000)]
number_generator = (x for x in range(100000000000000000000000000000000000))


# print(sys.getsizeof(list_number))
print(sys.getsizeof(number_generator))
   