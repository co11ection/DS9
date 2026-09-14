# ================ Рекурсия ===================
""" 
Рекурсия - это способ программирования при которой функция вызывает саму себя
для решения подзадачи
Обязательные элементы:
1) Базовая (условие остановки рекурсии)
2) Рекурсивный случай (вызов функции с упращенным аргументом)
"""

factorial = 5
result = 1
for i in range(1, factorial+1):
    result *= i
print(result)


def factorial_func(num: int) -> int:
    if num == 0:
        return 1
    return num * factorial_func(num-1)

print(factorial_func(4))

# 4 * factorial_func(3) -> 
# 4 * 3 * factorial_func(2) ->
# 4 * 3 * 2 * factorial_func(1)->
# 4 * 3 * 2 * 1 *  factorial_func(0)->
# 4 * 3 * 2 * 1 * 1->

# def a():
#     return "hi"
#     a()
# a()
# Не правильно!!! Причина нету оставки функции



list1 = [1, 2, 3, 4]
result = 0
for i in list1:
    result += i
print(result)


def sum_list(list1: list[int]) -> int:
    if not list1:
        return 0
    return list1[0] + sum_list(list1[1:])

print(sum_list(list1))
#1 + 2 + 3 + 4 + 0


list_sort = [1, 2, 3, 4, 5, 6, 7]
target = 4
for index, value in enumerate(list_sort):
    if not target in list_sort:
        print(-1)
        break
    if value == target:
        print(index)

list_sort = [1, 2, 3, 4, 5, 6, 7]
target = 4
def recursive_search(list_sort, target, index=0):
    if index >= len(list_sort):
        return -1
    if list_sort[index] == target:
        return index
    return recursive_search(list_sort, target, index+1)

print(recursive_search(list_sort, target))



list_sort = [1, 2, 3, 4, 5, 6, 7]
target = 6
def binary_search(list_sort: list[int], target: int, left=0, right=None) -> int:
    if right is None:
        right = len(list_sort) - 1
    
    if left > right:
        return -1
    
    mid = (left+right) // 2
    
    if list_sort[mid] == target:
        return mid
    elif target < list_sort[mid]:
        return binary_search(list_sort, target, left, mid-1)
    else:
        return binary_search(list_sort, target, mid+1, right)
    
print(binary_search(list_sort, target))
    

import sys
print(sys.getrecursionlimit())

sys.setrecursionlimit(3000)

print(sys.getrecursionlimit())