# Big O(n) - это про колличество операций алгоритма(функции) которую мы прописали
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] O(7)


def sum_list(list1):
    total = 0
    for i in list1:
        total += i
    return total

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_list(list1) # Big O(9)

#O(1) - константная сложность
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[0])

# O(n)
def sum_list(list1):
    total = 0
    for i in list1:
        total += i
    return total

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_list(list1) 

# O(n^2) - вложенные циклы
def has_duplicate(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i != j and lst[i] == lst[j]:
                return True
    return False
        
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9]
print(has_duplicate(list1))


#O(log n) - логорифмическая сложность 
# бинарный поиск


# O(n log n)
# O(2^n)

    
# def a(num):
#     if num == 0:
#         return
    
# a(0-1)
# a(0-1)


lst = [2,4,3,1,5]
# Пузырьковая сортировка - O(n^2)

def bubble_sort(lst):
    arr = lst.copy()
    lenght = len(arr)
    for i in range(lenght):
        for j in range(lenght-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort(lst))


# sorted O(n log n)
print(sorted(lst))