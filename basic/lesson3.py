# ========= List, tuple, set =========
""" 
list - изменяемые, индексируемыми, упорядоченный, итерируемым, неуникальный типом данных
можем представить как шкафчик с полками
литералы(обозначение) - []
 """

# Пример
list1 = ['груша', 'яблоко', 'банан']
list2 = ['груша', 'яблоко', 'банан', 3, 4, True, False]

# Индексация
list1 = ['груша', 'яблоко', 'банан']
print(list1[0])
print(list1[0:2])
print(list1[::2])

# Изменение
list1[0] = 'ананас'
print(list1)

print(len(list1))
print(len(list1[0]))

print('ананас' in list1)
print('груша' in list1)

# методы списка

# append - добавление элемента в спиок(в конец)
list1.append('мандарины')
print(list1)
# insert - вставка идет по индексу
list1.insert(1, 'киви')
print(list1)

# удаление
# remove
list1.remove('банан')
print(list1.pop(1)) # по дефолту удаляет последний элемент, но можно удалить и по индексу
print(list1)

list3 = [1, 2, 3, 4, 5]
list4 = [6, 7, 8, 9, 10]
list3.extend(list4)
print(list3)

list3.clear()
print(list3)

lst = [2, 1, 3, 5, 4, 6, 7, 8, 10, 9]
lst.sort(reverse=True)
print(lst)

# lst_copy = lst
# lst.append(0)
# print(lst)
# print('!!!!!!!!!!!!!!!!!!')
# print(lst_copy)

real_copy = lst.copy()
lst.append(0)
print(lst)
print('!!!!!!!!!!!!!!!!!!')
print(real_copy)


# tuple - неизменяемый, индексируемый, упорядоченный, итерируемый, неуникальный тип данных
# литералы - (,)
a = 1, 2
b = (1, 2,)
print(type(a))
print(type(b))

c, d = a
print(c)
print(d)

# set - изменяемым, неиндексируемый, неупорядоченный, уникальный, итерируемый тип данных
#литералы - {}

set1 = {1, 2, 1, 3, 2, 3, 4,}
print(set1)


a = 1
b = 1
print(id(a))
print(id(b))

ls1 = [1, 2, 3]
ls2 = [1, 2, 3]

print(id(ls1))
print(id(ls2))

set1 = {"hello", 1, 2, 1, 3, 2, 3, 4}
set1.add(5)
# set1.remove(3)
# set1.pop()
# set1."clear()
print(set1)

a = set()
print(type(a))

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print(set1 | set2) # обьединение
print(set1 & set2) # пересечение
print(set1 - set2) # разность (элементы set1 которых нет в set2)
print(set1 ^ set2) # симетричная разность (все элементы которые есть только в одном из множеств)
