# Цикл - повторение, позволяет выполнить одно и то же действие по несколько раз
# виды циклов
# For - перебирает итерируемые обьекты(типы данных)
# while - цикл который работает пока условие выдает True(иногда бывает бесконечной)

# Синтаксис for
# for <переменная которая хранит данные которые перебрала> in <итерируемый обьект(тип данных)>:
#     <тело цикла>


# for with str
counter = 0
string = 'Hello world'
for element in string:
    counter += 1
    
    print(element)
print(counter)

# for with range
for i in range(1, 11, 2):
    print(i)
    
# Найти сумму от 1 до 10(включительно)
result = 0
for i in range(1, 11):
    result += i
    
print(result)


list1 = [1,2,3,4,5,6,7,8,9,10, 11,12,13,14,15]
# перемножить все элементы друг на друга
result = 1
for num in list1:
    result *= num

print(result)

user = {
    "name": "John",
    'age': 20,
    "last_name": "Snow"
}

for key, value in user.items():
    print(key, "-->", value)
    
users = [
    {
    "name": "John",
    'age': 20,
    "last_name": "Snow"
},
    {
    "name": "Anya",
    'age': 17,
    "last_name": "Snow"
},
    {
    "name": "Aidar",
    'age': 14,
    "last_name": "Snow"
}
]



# while <условие>:
    # <тело>

num = 1

while num < 5:
    print(num)
    num +=1
    
list2 = []
num = 1
while num < 11:
    list2.append(num)
    num += 1
    print(list2)


# breake - оставливает цикл
list1 = [1,2,3,4,5,6,7,8,9, 11,12,13,14,10,15]
# запринтить до 10
for num in list1:
    if num == 10:
        break
    print(num)

# continue - пропускать ход(шаг, итерация, повторение)
list1 = [1,2,3,4,5,6,7,8,9, 11,12,13,14,10,15]
# запринтить кроме 10, 11, 8, 3 
for num in list1:
    if num in [10, 11, 8, 3 ]:
        continue
    print(num)

    

users = [
    {
    "name": "John",
    'age': 20,
    "last_name": "Snow"
},
    {
    "name": "Anya",
    'age': 17,
    "last_name": "Snow"
},
    {
    "name": "Aidar",
    'age': 14,
    "last_name": "Snow"
}
]

# for user in users:
#     if user['age'] >= 18:
#         print(f"{user['name']}  взрослый")
#     elif user['age'] < 18 and user['age'] > 14:
#         print(f"{user['name']} подросток")
#     else:
#         print(f"{user['name']} ребенок")

list1 = []
for i in range(1, 5):
    for j in range(1, 5):
        list1.append(j)
        print(i)
        print(list1)