#============== NumPy ===============
# NumPy - Это библиотека для быстрых вычислений с массивами(
# list, set, tuple 
# )

# В чем отличие Numpy от обычных list в python

a = [1, 2, 3]
b = [4, 5, 6]
print(a+b)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b)


# Создание массивов
# array
a = np.array([1, 2, 3])
print(a)

# zeros - чтобы массив состоял только из нулей
a = np.zeros(5)
print(a)

# ones
a = np.ones(3)
print(a)

# arange
a = np.arange(0, 10, 2)
print(a)

# linspace
a = np.linspace(0, 10, 5)
print(a)


# Размерность массивов
# 1D - одномерный
"""
[1 2 3] - как обычный список
"""
#2D - двухмерный массив
""" 
[
    [1 2 3],
    [4 5 6]
]
"""
# 3D - трехмерный массив
""" 
[
    [
        [1 2 3],
        [4 5 6]
    ],
    [
        [7 8 9],
        [10 11 12]
    ]
]
"""

#1D
a = np.array([1, 2, 3])
print(a)

# 2D
a = np.zeros((2, 3))
print(a)

#3D
a = np.zeros((2, 3, 5))
print(a)

# Атрибуты

a = np.array(
    [
        [1, 2 ,3],
        [4, 5, 6]
    ]
)
# Размерность
print(a.shape) #(2, 3)
# Многомерность
print(a.ndim) #2
#Колличество элементов
print(a.size) #6
# Проверка типа данных 
print(a.dtype) #int64

# =========== Индексация и срезы =====
# Одномерный массив
arr = np.array([1, 2, 3])
print(arr[0])
print(arr[1: ])

# Двухмерный массив
arr = np.array(
    [
        [1,2,3],
        [4,5,6]
    ]
)
# формат: строка, столбец
print(arr[0, 0])
print(arr[1, 1])
print(arr[0][1])
print(arr[0][1: ])

#====== Арифматические операции ====
arr = np.array([1, 2, 3])

print(arr + 1)
print(arr * 2)

# Агрегатные функции
arr = np.array([1, 2, 3])
print(arr.sum())
print(arr.mean())
print(arr.max())
print(arr.min())

# ========== изменение формы ============
arr = np.arange(6)
print(arr)
arr2 = arr.reshape(2, 3)
print(arr2)
arr2 = arr.reshape(3, 2)
print(arr2)

# --- Рандом ---
arr = np.random.rand(3,3)
print(arr)

# ============= Практика =============
# # Создать массив из числе 1-10 (включительно)
# arr = np.arange(1, 11)
# print(arr)

# # возвести в квадрат
# print(arr ** 2)

# # созддать массив и изменить его форму на 3х3
# arr = np.arange(9)
# arr2 = arr.reshape(3,3)
# print(arr2)

# """ 
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

#  [
#      [1]
#      [4]
#      [7]
#  ]
# """

# # Получить второй столбец
# print(arr2[:, 1])
# print(arr2[:, 1:2])


